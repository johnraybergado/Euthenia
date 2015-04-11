/**
 *
 * DATA SOURCE:  http://www.census.gov/foreign-trade/statistics/country/
 *
 */

function fetchData() {
    d3.csv("us.csv", function(csv) {
        VisDock.startChrome();
        var normalized=[];

        for (var i=0; i < csv.length; i++)  {
		    
            var row=csv[i];
            var newRow={};
			
			
			
		     newRow.Year=row.Year;
             newRow.Country=row.PartnerCountries;
			 newRow.Imports=Number(row["Import"]);
             newRow.Exports=Number(row["Export"]);
		     normalized.push(newRow);
		     
		   
        }

        countriesGrouped = d3.nest()
            .key(function(d) { return d.Year; })
            .key(function(d) { return d.Month; })
            .entries(normalized);

        //Sum total deficit for each month
        var totalImport=0;
        var totalExport=0;

        for (var y=0; y < countriesGrouped.length; y++) {
            var yearGroup=countriesGrouped[y];
            for (var m=0; m < yearGroup.values.length; m++) {
                var monthGroup=yearGroup.values[m];
                for (var c=0; c < monthGroup.values.length; c++) {
                    var country=monthGroup.values[c];
                    totalImport= Number(totalImport) + Number(country.Imports)*10000000;
                    totalExport=Number(totalExport) + Number(country.Exports)*10000000;
                }
                //    console.log("totalExport=" + String(totalExport));
                monthlyExports.push(totalExport);
                monthlyImports.push(totalImport);
            }

        }

        //Start running
        run();
        refreshIntervalId = setInterval(run, delay);
        // run();
        VisDock.finishCHrome();
    });

}