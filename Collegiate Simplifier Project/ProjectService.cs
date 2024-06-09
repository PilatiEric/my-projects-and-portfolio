/*******************************************************************************************************************
* ProjectService.cs Sample
*
* These are a few examples of queries written to help pull information from our SQL Server
********************************************************************************************************************/


 internal IEnumerable<Cost> Adjustments(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT p.Id, v.vendorname, p.PurchaseOrderNumber, p.TotalPrice, p.Materials, p.ProcessDate, 
                            p.ContractNumber, p.RequisitionNumber, v.VendorName, p.PSNumber
                     FROM Costs p 
                     LEFT JOIN Vendors v ON p.VendorId = v.Id
                     WHERE p.ProjectId = @ProjectId 
                       AND Commitmenttype = 'Adjustment' 
                     ORDER BY v.VendorName, p.ProcessDate";

         return connection.QueryAsync<Cost>(sql, new { ProjectId = id }).Result;
     }
 }



 /// <summary>
 /// Gets all Commitments from the Costs table that
 /// have a Status of "Pending".
 /// </summary>
 /// <param name="id"></param>
 /// <returns>A list of Commitments</returns>
 internal IEnumerable<Cost> PendingPOs(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT p.Id, p.PurchaseOrderNumber, p.TotalPrice, p.Materials, p.ProcessDate, 
                            p.ContractNumber, p.RequisitionNumber, v.VendorName, p.PSNumber,
                            (SELECT ISNULL(SUM(ts.invoicetotal),0)
                             FROM Invoices AS ts 
                             WHERE ts.costid = p.id) AS InvTotal
                     FROM Costs p 
                     LEFT JOIN Vendors v ON p.VendorId = v.Id
                     WHERE p.ProjectId = @ProjectId 
                       AND p.RequisitionNumber IS NULL 
                       AND Status = 'Pending'                             
                     ORDER BY v.VendorName, p.ProcessDate";

         return connection.QueryAsync<Cost>(sql, new { ProjectId = id }).Result;
     }
 }



 //ApprovedPOs: Pulls information for all Simplifier purchase orders
 //             from Costs table whose status = "Approved"
 internal IEnumerable<Cost> ApprovedPOs(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT p.Id, p.PurchaseOrderNumber, p.TotalPrice, p.Materials, p.ProcessDate, 
                            p.ContractNumber, p.RequisitionNumber, v.VendorName, p.PSNumber,
                            (SELECT ISNULL(SUM(ts.invoicetotal),0)
                             FROM Invoices AS ts 
                             WHERE ts.costid = p.id) AS InvTotal
                     FROM Costs p 
                     LEFT JOIN Vendors v ON p.VendorId = v.Id
                     WHERE p.ProjectId = @ProjectId 
                       AND p.RequisitionNumber IS NULL 
                       AND Status = 'Approved' 
                     ORDER BY v.VendorName, p.ProcessDate";

         return connection.QueryAsync<Cost>(sql, new { ProjectId = id }).Result;
     }
 }



 internal IEnumerable<Cost> ApprovedPOsPS(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT p.Id, p.PurchaseOrderNumber, p.TotalPrice, p.Materials, p.ProcessDate, 
                            p.ContractNumber, p.RequisitionNumber, v.VendorName
                     FROM Costs p 
                     LEFT JOIN Vendors v ON p.VendorId = v.Id
                     WHERE p.ProjectId = @ProjectId 
                       AND p.RequisitionNumber = NULL 
                       AND Status = 'Approved' 
                     ORDER BY v.VendorName, p.ProcessDate";

         return connection.QueryAsync<Cost>(sql, new { ProjectId = id }).Result;
     }
 }



 //PlaceholderPOs: Pulls information for all Simplifier purchase orders
 //                from Costs table whose status = "Placeholder"
 internal IEnumerable<Cost> PlaceholderPOs(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT p.Id, p.PurchaseOrderNumber, p.TotalPrice, p.Materials, p.ProcessDate, v.VendorName,
                            p.RequisitionNumber, p.PSNumber, t.ReqId
                     FROM Costs p 
                     LEFT JOIN AccountTransactions t ON t.PONo = p.PSNumber
                     LEFT JOIN Vendors v ON p.VendorId = v.Id
                     WHERE p.ProjectId = @ProjectId 
                       AND CommitmentType = 'Placeholder' 
                     ORDER BY v.VendorName, p.ProcessDate";

         return connection.QueryAsync<Cost>(sql, new { ProjectId = id }).Result;
     }
 }



 //PendingChanges: 
 internal IEnumerable<Change> PendingChanges(int id)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT ch.*, cn.Name
                     FROM ContractChanges ch 
                     LEFT JOIN Contractors cn ON ch.ContractorId = cn.Id
                     WHERE ch.ProjectId = @ProjectId 
                       AND CoNum IS NULL 
                       AND Status != 'Rejected' 
                     ORDER BY cn.Name, ch.PcoNum";

         return connection.QueryAsync<Change>(sql, new { ProjectId = id }).Result;
     }
 }



 internal IEnumerable<Change> ApprovedChanges(int ProjectId)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT ch.*, cn.Name
                     FROM ContractChanges ch 
                     LEFT JOIN Contractors cn ON ch.ContractorId = cn.Id
                     WHERE ch.ProjectId=@ProjectId 
                       AND CoNum IS NULL 
                       AND Status = 'Approved' 
                     ORDER BY cn.Name, ch.PcoNum";

         return connection.QueryAsync<Change>(sql, new { ProjectId }).Result;
     }
 }



 internal IEnumerable<Change> ApprovedCO(int ProjectId)
 {
     using (var connection = new SqlConnection(_configuration.GetConnectionString("DefaultConnection")))
     {

         var sql = @"SELECT ch.*, cn.Name
                     FROM ContractChanges ch 
                     LEFT JOIN Contractors cn ON ch.ContractorId = cn.Id
                     WHERE ch.ProjectId=@ProjectId 
                       AND Status = 'Approved' 
                     ORDER BY cn.Name, ch.PcoNum";

         return connection.QueryAsync<Change>(sql, new { ProjectId }).Result;
     }
 }
