$(document).ready(function(){

	$("#aspect_display > li").mCustomScrollbar({scrollButtons:{enable:true}, theme:"dark"});
	$("#aspect_pager").mCustomScrollbar({scrollButtons:{enable:false}, autoHideScrollbar: true, theme:"light"});
	
	$("#aspect_pager li:first").addClass('current');
	$("#aspect_display > li:first").addClass('displayed');

	$(".content_editor").cleditor();

	
	$(".edit_content").click(function(){
		content=$(this).parents('header').next().find('.content_text').html();
		$(this).parents('header').next().find('.content_text').hide();
		$(this).hide();
		$(this).parents('header').next().find('.edit_content_form').slideDown();
		$(this).parents('header').next().find(".content_editor").val(content);
		editor= $(this).parents('header').next().find(".content_editor").cleditor()[0];
		editor.refresh()
	});

	$(".cancel").click(function(event){
		event.preventDefault();

		content=$(".content_editor").val();
		$(this).parents('.container').prev().find('.edit_content').show();
		$(this).parent().parent().find('.content_text').html(content);
		$(this).parent().parent().find('.content_text, .edit_content').show();
		$(this).parent().parent().find('.edit_content_form').slideUp();
		//$(this).parent().find(".content_editor").val(content);
		//editor= $(this).parent().find(".content_editor").cleditor()[0];
		//editor.refresh()

	});

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
			$("#aspect_content").cleditor();
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

	$('.edit_textarea').editable(function(value, settings) { 
		$("#member_description").val(value);
		$("#project_description").val(value);
		$("#product_description").val(value);
		return(value);
	}, { 
		type    : 'textarea',
		submit  : 'OK',
	});

	$('#edit_name').editable(function(value, settings) { 
		$("#member_name").val(value);
		$("#project_title").val(value);
		$("#product_title").val(value);
		return(value);
	}, { 
		type    : 'text',
		submit  : 'OK',
	});

	$('#edit_lastname').editable(function(value, settings) { 
		$("#member_lastname").val(value);
		return(value);
	}, { 
		type    : 'text',
		submit  : 'OK',
	});


	$('.edit_charge').editable(function(value, settings) { 
		$("#member_charge").val(value);
		return(value);
	}, { 
		data   : " {'Director':'Director','Semillero':'Semillero','Investigador':'Investigador', 'selected':'Director'}",
		type   : 'select',
		submit : 'OK'
	});

	$('.edit_status').editable(function(value, settings) { 
		$("#project_status").val(value);
		return(value);
	}, { 
		data   : " {'Activo':'Activo','Terminado':'Terminado','selected':'Activo'}",
		type   : 'select',
		submit : 'OK'
	});

	$(".link_editable").editable(function(value, settings) { 
		$("#member_cvlac").val(value);
		$("#project_moreurl").val(value);
		$("#product_moreurl").val(value);
		return(value);
	}, { 
		type      : "text",
		tooltip   : "Move mouseover to edit...",
		event     : "click",
		submit : 'OK'
	});

	$(".thumbnail img").click(function(){
		$("#member_image").click();
		$("#project_image").click();
		$("#product_image").click();
	});
});


