$(document).ready(function(){

	$("#aspect_display > li").mCustomScrollbar({scrollButtons:{enable:true}, theme:"dark"});
	
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

	$("#setlang li a").click(function(){
		$("#lang").val($(this).attr('lang'));
		$("#setlang_form").submit();
	});

	var toggledAdd=false;
	var toggledEdit=false;

	$("#btn_add_slide").click(function(){
		if(toggledEdit){
			$("#edit_slide_form").stop().slideUp();
			toggledEdit=false;
		}
		if(toggledAdd){
			$("#add_slide_form").slideUp();
			toggledAdd=false;
		}else{
			$("#add_slide_form").slideDown();
			toggledAdd=true;
		}
	})

	$("#btn_edit_slide").click(function(){
		if(toggledAdd){
			$("#add_slide_form").stop().slideUp();
			toggledAdd=false;
		}
		if(toggledEdit){
			$("#edit_slide_form").slideUp();
			toggledEdit=false;
		}else{

			alert($('.showed').html());

			title=$('.showed .slide_title').html();
			id=$('.showed').attr('id');
			name=$('.showed').attr('name');
			index=$('.showed').attr('index');
			link=$('.showed').attr('link');
			abstract=$('.showed .slide_abstract').html();

			$("#ed_slide_id").val(id);
			$("#ed_slide_name").val(name);
			$("#ed_slide_title").val(title);
			$("#ed_slide_abstract").val(abstract);
			$("#ed_slide_index").val(index);
			$("#ed_slide_link").val(link);
		

			$("#edit_slide_form").slideDown();
			toggledEdit=true;
		}
	});

	$("#btn_del_slide").click(function(){
		document.location.href='eliminar_slide/'+$('.showed').attr('id');
	});

	$("#zo").click(function(e){
		e.preventDefault()
		$("#z").click();
	})

	$("#zob").click(function(e){
		e.preventDefault()
		$("#zp").click();
	})

	$("#zu").click(function(e){
		e.preventDefault()
		$("#z2u").click();
	})

	$("#zub").click(function(e){
		e.preventDefault()
		$("#zup").click();
	})

	$("#aspect_pager li").click(function(){
		$(this).addClass('current').siblings().removeClass('current');
		id = $(this).attr('aspect');	
		
		$("#"+id).siblings().slideUp(500, function(){
			
			$("#"+id).slideDown(1000, function(){
			});
		});
		// $("#aspect_display li").mCustomScrollbar("update");
	});
});


var load_data=function(slide){

}