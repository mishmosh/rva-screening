window.App = window.App || {};

var AppController = function ( options ) {
  console.info('APP INITIALIZED :)');
  this.options = options || {};
  this.waka = 'flaka';
  this.hiphip = 'hooray!';
  console.log(this);
};

function addNewInputRow($table, $input_row) {
	current_length = $input_row.length;
	$new_row = $input_row.clone();
	$new_row.each(function() {
		this.id += current_length;
		// $(this).find("input").each(function() {
		// 	this.name +=current_length;
		// })
	})
	$table.append($new_row);
	return;
}

function showHiddenFields() {
	$(event.target).parent().siblings().each(
		function() {
			$(this).find(".hidden-input").show().prop('disabled', false);
			$(this).find(".read-only").hide().prop('disabled', true);
		}
	);
}
window.app = window.app || {};

AppController = function ( options ) {
  this.options = options || {};

  console.info('APP INITIALIZED :)');

  // this.addEventHandlers();

  // this.addEventHandlers = function () {
  //   var menu = document.getElementById('menu-expand');
  // }
}

