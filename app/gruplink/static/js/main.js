$(document).ready(function(){
	
	$("#submit_section_updates").click(function(event){

		event.preventDefault();

		var table="";
		$("#sections_edit_fields tr ").each(function(){
			
			var row=$(this).find('td:first').html()+",";
			$(this).find('td input').each(function(){
				row+=$(this).val()+","
			});
			row=row.substr(0, row.length-1);
			table+=row+";";
		});
		$("#data").val(table.substr(0, table.length-1));
		$("#update_sections_form").submit();
	});
});