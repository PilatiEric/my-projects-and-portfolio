@{
/***********************************************************************************************************************************************************
*  Edit Commitment page
*
*  This page is part of a site built to handle the various financial and logistical aspects of projects across multiple campuses and buildings.
*
*
*  This is the back-end section of a page that allows the user to edit an existing "commitment" or purchase order. Not shown are the various services
*  and SQL queries needed to pull the data from a Microsoft SQL Server and configure it to needed specifications.
***********************************************************************************************************************************************************/
}

using Microsoft.AspNetCore.DataProtection;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.WebUtilities;
using SanDiego.Models;
using SanDiego.Services;
using SanDiego.Utility;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Net.Mail;
using System.Text;


namespace PlaceholderName.Pages.Planning
{
    public class CostEditModel : PageModel
    {
        #region Fields

        #region Services
        //SERVICES
        private AccountingService db;
        private ProjectService db2;
        private UserService userServ;
        private DocumentsService docsServ;
        private CostApprovalEscalationService escalationServ;
        private readonly IDataProtectionProvider _dataProtectionProvider;
        private readonly IEmailSender mail;
        private readonly IWebHostEnvironment _hostEnvironment;
        //private IHttpContextAccessor hca;
        public BreadcrumbService BreadcrumbService { get; }
        #endregion

        #region Lists
        //LISTS
        [BindProperty]
        public List<SelectListItem> LstStatus { get; set; }

        [BindProperty]
        public List<IFormFile> Uploads { get; set; }
        #endregion

        #region IEnumerables
        //IENUMERABLES

        [BindProperty]
        public IEnumerable<Vendor> Vendors { get; set; }
        [BindProperty]
        public IEnumerable<ProjectAccountingSummary> Accounts { get; set; }

        #endregion

        #region Input Fields
        //INPUT FIELDS
        [BindProperty]
        public string VendorName { get; set; }

        [BindProperty]
        public string StatusWas { get; set; }

        [BindProperty]
        public string ContractNumber { get; set; }

        [BindProperty]
        public string CommitmentType { get; set; }

        [BindProperty]
        public string PSStatus { get; set; }
        public string PSNumber { get; set; }
        #endregion


        #region Validations
        //VALIDATIONS
        public string ErrorMessage { get; set; }
        public string ContractNumValidation { get; set; }

        public string PSStatusValidation { get; set; }
        public string Mesg { get; set; }
        #endregion


        [BindProperty]
        public Cost PO { get; set; }

        [BindProperty]
        public ProjectShort PS { get; set; }

        public SiteUser Usr { get; set; }

        [BindProperty(SupportsGet = true)]
        public int id { get; set; }



        #endregion



        #region CostEditModel
        public CostEditModel(AccountingService dbServ,
                             ProjectService dbServ2,
                             UserService dbServ3,
                             UserService us,
                             CostApprovalEscalationService costApprovalEscalationService,
                             BreadcrumbService breadcrumbService,
                             IWebHostEnvironment webHostEnvironment,
                             IEmailSender mailServ,
                             IHttpContextAccessor accessor,
                             IDataProtectionProvider dataProtectionProvider)
        {
            db = dbServ;
            db2 = dbServ2;
            userServ = dbServ3;
            // hca = accessor;
            mail = mailServ;
            userServ = us;
            escalationServ = costApprovalEscalationService;
            _dataProtectionProvider = dataProtectionProvider;
            BreadcrumbService = breadcrumbService;
            _hostEnvironment = webHostEnvironment;
        }
        #endregion



        public IActionResult OnGet(string poid,
                                   string msg = null)
        {
            int decrpPoId = DataProtector.DecryptId(_dataProtectionProvider, poid);
            PO = db2.POItem(decrpPoId);
            PS = db2.ProjectShort(PO.ProjectId);
            Vendors = db.VendorsAll();
            //Usr = userServ.GetByUserName(hca.HttpContext.User.Identity.Name);
            Accounts = db.ProjectAccounts(PS.PsProjId).OrderBy(x => x.ClassDescr);



            StatusWas = PO.Status;
            Mesg = msg ?? msg;

            if (escalationServ.IsCostSendForApproval(decrpPoId))
            {
                return RedirectToPage("/planning/cost", new
                {
                    poid = DataProtector.EncryptId(_dataProtectionProvider, PO.Id),
                    msg = "Commitment forwarded for Approval. Cannot Modify."
                });
            }

            #region Breadcrumb
            BreadcrumbService.AddBreadcrumb("LRCP", "/Planning/LRCP");
            BreadcrumbService.AddBreadcrumb("SBS", "/Planning/SBS?id=" + DataProtector.EncryptId(_dataProtectionProvider, PO.ProjectId));
            BreadcrumbService.AddBreadcrumb("Costs Log", "/Planning/CostsLog?id=" + DataProtector.EncryptId(_dataProtectionProvider, PO.ProjectId));
            BreadcrumbService.AddBreadcrumb("Cost", "/Planning/Cost?poid=" + poid);
            BreadcrumbService.AddBreadcrumb("Cost Edit", "/Planning/CostEdit?poid=" + poid);
            #endregion
            return Page();
        }



        public IActionResult OnPostAsync()
        {

            #region Delete Commitment
            string delete = Request.Form["deletePO"];
            if (delete == "DeleteThisPO")
            {
                int poid = PO.Id; // int.Parse(Request.Form["Model.Project.Id"]);

                db2.DeletePO(poid);

                return RedirectToPage("/planning/CostsLog", new { id = DataProtector.EncryptId(_dataProtectionProvider, PO.ProjectId),
                                                                  msg = "Commitment item has been deleted."
                                                                });
            }
            #endregion

            if (PO.CommitmentType == "Contract" &&
                string.IsNullOrEmpty(PO.ContractNumber))
            {
                ModelState.AddModelError("ContractNumValidation",
                                         "Contract # is required");
            }

            if (string.IsNullOrEmpty(PO.PSStatus))
            {
                ModelState.AddModelError("PSStatusValidation",
                                         "PSStatus # is required");
            }

            if (ModelState.IsValid)
            {
                try
                {
                    #region File Upload
                    //FILE UPLOAD DESCRIPTION
                    //This handles the uploading of files
                    //It will check if the directory for the specific project exists
                    //If not, it will create a new directory for the specific project


                    //TODO: Create function on DocumentService that updates line with matching file information
                    foreach (IFormFile uploadedFile in Uploads)
                    {
                        if (uploadedFile.ContentType != null &&
                            uploadedFile.Length > 0)
                        {
                            // Process and save the uploaded file, similar to CostNew
                            var fileName = uploadedFile.FileName;
                            var filePath = Path.Combine(@_hostEnvironment.ContentRootPath,
                                                        "DataStorage",
                                                        "ProjectDocuments",
                                                        PO.ProjectId.ToString(),
                                                        fileName);

                            if (!Directory.Exists(Path.Combine(@_hostEnvironment.ContentRootPath,
                                                               "DataStorage",
                                                               "ProjectDocuments",
                                                               PO.ProjectId.ToString())))
                            {
                                Directory.CreateDirectory(Path.Combine(@_hostEnvironment.ContentRootPath,
                                                                       "DataStorage",
                                                                       "ProjectDocuments",
                                                                       PO.ProjectId.ToString()));
                            }

                            using (var stream = new FileStream(filePath, FileMode.Create))
                            {
                                uploadedFile.CopyTo(stream);
                                PO.FileName = Path.Combine("/DataStorage",
                                                           "ProjectDocuments",
                                                           PO.ProjectId.ToString(),
                                                           fileName);
                            }
                        }
                    }
                    #endregion

                    db2.UpdatePO(PO);

                    #region escalate
                    var saveSubmit = Request.Form["SaveSubmit"];
                    if (PO.Id > 0 &&
                        PO.Status == "Pending" &&
                        saveSubmit == "SendToApproval" &&
                        !escalationServ.IsCostSendForApproval(PO.Id))
                    {
                        if (!escalationServ.IsRoutingConfigured(PO.ProjectId))
                        {
                            return RedirectToPage("/planning/cost", new { poid = DataProtector.EncryptId(_dataProtectionProvider, PO.Id),
                                                                          msg = "Routing Configuration Not found for the Project."
                                                                        });
                        }

                        CostApprovalEscalation approver = escalationServ.GetNextApprover(PO.Id);

                        if (approver.ApproverId > 0)
                        {
                            var res = escalationServ.AddCostForApproval( new CostApprovals { CostId = PO.Id,
                                                                                             CreatedDate = DateTime.Now,
                                                                                             ApproverId = approver.ApproverId,
                                                                                             EscalationOrder = approver.EscalationOrder,
                                                                                             Remarks = "",
                                                                                             Status = "Pending"
                                                                                           });
                            if (res > 0)
                            {
                                var code = escalationServ.GenerateCostApprovalToken(res.ToString());
                                code = WebEncoders.Base64UrlEncode(Encoding.UTF8.GetBytes(code));
                                var callbackUrl = Url.Page( "/Planning/POCostMailApproval",
                                                            pageHandler: null,
                                                            values: new { CostId = DataProtector.EncryptId(_dataProtectionProvider, PO.Id), approvalId = @DataProtector.EncryptId(_dataProtectionProvider, res), code },
                                                            protocol: Request.Scheme);
                                escalationServ.SendMail(escalationServ.GetById(res), callbackUrl);
                            }
                        }
                    }
                    #endregion
                }
                catch (SqlException e)
                {
                    var mesg = e.Message;
                    return RedirectToPage("/Error", new { Err = mesg });
                }

                if (StatusWas == "Pending" &&
                    PO.Status == "Approved")
                {
                    string pmEmail = userServ.GetById(PO.RequestorId).Email;
                    MailMessage mm = new MailMessage();
                    mm.To.Add(pmEmail);
                    mm.Subject = "Commitment Approval";
                    mm.Body = "Hi there, <br />" +
                              "A Commitment you requested, in Simplifier, has been approved:<br />" +
                              "Project: " + PS.CampusAbrev + " " + PS.ProjectTitle + "<br />" +
                              "Project #: " + PS.ProjectId + "<br />" +
                              "Contract #: " + ContractNumber + "<br />" +
                              "Vendor: " + VendorName + "<br />" +
                              "Total Amount: " + PO.TotalPrice + "<br />" +
                              "Date: " + PO.ProcessDate + "<br />" +
                              "Funding Source: " + "<br />" + //NEEDS TO BE ADDED
                              "PS Fund #: " + PO.PSNumber + "<br />" +
                              "This email was generated by Simplifier.";

                    mail.SendEmailAsync(mm); // uncomment in production
                }
                return RedirectToPage("/planning/Cost", new { poid = DataProtector.EncryptId(_dataProtectionProvider, PO.Id),
                                                              msg = "Cost item has been saved."
                                                            });
            }
            
            return Page();
        }
    }
}
