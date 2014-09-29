$(function(){
	$('.addbtn').click(buttonHandler);
	$('.js-delete').click(deleteHandler);
	$('.js-check').click(checkClick);
	startWatch();
	setInterval(startWatch, 3000);
	checkForDone();
})

function checkForDone() {
	$('.todo-container').each(function(index, elem) {
		if (elem.getAttribute('value') == 'True') {
			setTodoInactive(elem.id);
		}	
	});
}

function startWatch() {
	var deadedTodo = [];
	var time = (new Date).getTime()/1000 + "";
	time = parseInt(time.split('.')[0]);
	$('div.timestamp').each(function(index, elem) {
		if (parseInt(elem.getAttribute('value')) < time) {
			deadedTodo.push(elem.id);
		}
	});
	deadedTodo.forEach(function(index) {
		$('div#' + index).children().css('border-top', '5px solid rgb(235, 125, 114)')
	})
}

function setTodoInactive(id) {
	$('div#' + id).css('opacity', '0.4');
	$('.js-checkicon').filter('#' + id).removeClass('fa-square-o').addClass('fa-check-square-o');
	$('.js-check').filter('#' + id).attr('disabled', 'disabled');
}

function checkClick(event) {
	$.post("api/check", {id: event.target.id}).done(function( data ) {
		if (data.isdone) {
			setTodoInactive(event.target.id);
		}
	});
}

function buttonHandler(event) {
	var author = $('.input-name');
	var title = $('#title');
	var text = $('#text');
	var timeField = $('#deadline');
	if (!checkIsEmpty()) {
		var time = parseDate(timeField.val());
		var data = {
			author : author.val() || 'Incognito',
			title : title.val(),
			text : text.val(),
			month: time.month, 
			day: time.day, 
			year: time.year, 
			hrs: time.hrs, 
			mins: time.mins, 
			sec: time.sec
		};
		$.post("api/add", data).done(function( data ) {
			$('.add-js').after(data);
			author.val('')
			title.val('');
			text.val('');
			timeField.val('');
			$('.js-delete').click(deleteHandler);
			$('.js-check').click(checkClick)
  		});
	} else {
		showError();
	}
}

function deleteHandler(event) {
	var iddata = {
		id: event.target.id
	}
	$.post("api/delete", iddata).done(function( data ) {
		$('div#' + data.id).remove();
	});
}

function checkIsEmpty() {
	var title = $('#title');
	var datetime = $('#deadline');
	return !(title.val() && datetime.val());
}

function showError() {
	var errBlock = $('.js-alert');
	errBlock.css('display', 'block');
	setTimeout(function() {
		errBlock.css('display', 'none');
	}, 5000)
}

function parseDate(date) {
	var obj = {
		month: 0, 
		day: 0, 
		year: 0, 
		hrs: 0, 
		mins: 0, 
		sec: 0
	};
	var arr = date.split('/');
	obj.month = parseInt(arr[0]);
	obj.day = parseInt(arr[1]);
	obj.year = parseInt(arr[2].split(' ')[0]);
	var pmam = arr[2].split(' ')[2];
	arr = arr[2].split(' ')[1];
	if (pmam == 'PM') {
		obj.hrs = parseInt(arr.split(':')[0]) + 12;
		if (obj.hrs == 24) obj.hrs = 0;
	} else {
		obj.hrs = parseInt(arr.split(':')[0]);
	}
	obj.mins = parseInt(arr.split(':')[1]);
	obj.sec = parseInt(arr.split(':')[2]);
	return obj;
}