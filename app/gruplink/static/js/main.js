$(document).ready(function(){

	$("#aspect_display > li").mCustomScrollbar({scrollButtons:{enable:true}, theme:"dark"});
	$("#aspect_pager").mCustomScrollbar({scrollButtons:{enable:false}, autoHideScrollbar: true, theme:"light"});
	
	$("#aspect_pager li:first").addClass('current');
	$("#aspect_display > li:first").addClass('displayed');

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
	});

	var toggledAddB=false;
	var toggledEditB=false;

	$("#btn_add_aspect").click(function(){
		if(toggledEditB){
			$("#edit_aspect_form").stop().slideUp();
			toggledEdit=false;
		}
		if(toggledAddB){
			$("#add_aspect_form").slideUp();
			toggledAddB=false;
		}else{
			$("#add_aspect_form").slideDown();
			$("#aspect_content").cleditor({width:'auto'});
			toggledAddB=true;
		}
	});


	$("#btn_edit_slide").click(function(){
		if(toggledAdd){
			$("#add_slide_form").stop().slideUp();
			toggledAdd=false;
		}
		if(toggledEdit){
			$("#edit_slide_form").slideUp();
			toggledEdit=false;
		}else{
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

	var editor;

	$("#btn_edit_aspect").click(function(){
		if(toggledAddB){
			$("#add_aspect_form").stop().slideUp();
			toggledAddB=false;
		}
		if(toggledEditB){
			$("#edit_aspect_form").slideUp();
			toggledEditB=false;
		}else{

			id=$('.displayed').attr('aspect-id');
			index=$('.displayed').attr('index');
			icon=$('#aspect_pager .current i').attr('class');
			title=$('.displayed .aspect_title').html();
			content=$('.displayed .aspect_content').html();
			
			$("#ed_id").val(id);
			$("#ed_icon").val(icon);
			$("#ed_title").val(title);
			$('#ed_content').val(content);
			$('#ed_index').val(index);

			$("#edit_aspect_form").slideDown();
			
			editor=$("#ed_content").cleditor()[0];

			editor.refresh();

			toggledEditB=true;
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
			
			$("#"+id).slideDown(1000).addClass('displayed');
		}).removeClass('displayed');
		// $("#aspect_display li").mCustomScrollbar("update");
		
		$("#add_aspect_form, #edit_aspect_form").slideUp(500);

	});

	$('#btn_del_aspect').click(function(){
		document.location.href='eliminar_slide/'+$('.displayed').attr('aspect-id');
	});

});


var load_data=function(slide){

}