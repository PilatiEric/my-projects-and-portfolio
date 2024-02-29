@{
/***********************************************************************************************************************************************************
*  New Project Page
*
*  This page invoved the use of a cascading dropdown menu to create a new project in which new commitments, invoices, etc. could be assigned to.
*  Depending on the selection made in the campus dropdown menu, the building menu would be populated with different selections.
*  This required the use of SQL queries that pulled from two seperate databases in order two fully function - one hosted campus information and the other buildings.
*
*
*  This is the back-end section of a page that allows the user to choose which campus and building on that campus that would be the focus of the project.
*  Not shown are the various functions and SQL queries called to in the Service files.
***********************************************************************************************************************************************************/
}

using Microsoft.AspNetCore.DataProtection;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using SanDiego.Models;
using SanDiego.Services;
using SanDiego.Utility;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace SanDiego.Pages.Planning
{
    public class SBSNewModel : PageModel
    {
        public ProjectService db;
        public InventoryService db2;
        private UserService currentUser;
        private readonly IDataProtectionProvider _dataProtectionProvider;
        private readonly InventoryService _inventoryService;
        public IEnumerable<Campus> Colleges { get; private set; }
        public IEnumerable<Building> CampusBuildings { get; set; }
        public IEnumerable<Building> BuildingsByCampusList { get; private set; }
        [BindProperty]
        public string ProjectTitle { get; set; }
        [BindProperty]
        public string SelectedCollege { get; set; }
        public string SelectedBuilding { get; set; }
        public BreadcrumbService BreadcrumbService { get; }

        public SBSNewModel(ProjectService dbServ, 
                           UserService cUser, 
                           InventoryService inventoryService, 
                           BreadcrumbService breadcrumbService, 
                           IDataProtectionProvider dataProtectionProvider)
        {
            db = dbServ;
            _inventoryService = inventoryService;
            currentUser = cUser;
            BreadcrumbService = breadcrumbService;
            _dataProtectionProvider = dataProtectionProvider;
        }
        

        public async Task<IActionResult> OnGet()
        {
            BreadcrumbService.AddBreadcrumb("LRCP", "/Planning/LRCP");
            BreadcrumbService.AddBreadcrumb("NewProject", "/Planning/SBSNew");

            if (currentUser.Role != "Admin")
            {
                return StatusCode(403);
            }
            Colleges = await db.GetAllCampuses();
            return Page();
        }
        public IActionResult OnPost(string selectedBuilding)
        {
            int collegeId = Convert.ToInt32(SelectedCollege.Substring(0, 4));
            int newPid = db.AddNewProject(collegeId, ProjectTitle, selectedBuilding);
            return RedirectToPage("/planning/sbsedit", new { id = DataProtector.EncryptId(_dataProtectionProvider, newPid) });

        }
    }
}
