/*
	Editorial by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/


(function($) {

	var	$window = $(window),
		$head = $('head'),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ '361px',   '480px'  ],
			xxsmall:  [ null,      '360px'  ],
			'xlarge-to-max':    '(min-width: 1681px)',
			'small-to-xlarge':  '(min-width: 481px) and (max-width: 1680px)'
		});

	// Stops animations/transitions until the page has ...

		// ... loaded.
			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-preload');
				}, 100);
			});

		// ... stopped resizing.
			var resizeTimeout;

			$window.on('resize', function() {

				// Mark as resizing.
					$body.addClass('is-resizing');

				// Unmark after delay.
					clearTimeout(resizeTimeout);

					resizeTimeout = setTimeout(function() {
						$body.removeClass('is-resizing');
					}, 100);

			});

	// Fixes.

		// Object fit images.
			if (!browser.canUse('object-fit')
			||	browser.name == 'safari')
				$('.image.object').each(function() {

					var $this = $(this),
						$img = $this.children('img');

					// Hide original image.
						$img.css('opacity', '0');

					// Set background.
						$this
							.css('background-image', 'url("' + $img.attr('src') + '")')
							.css('background-size', $img.css('object-fit') ? $img.css('object-fit') : 'cover')
							.css('background-position', $img.css('object-position') ? $img.css('object-position') : 'center');

				});

	// Sidebar.
		var $sidebar = $('#sidebar'),
			$sidebar_inner = $sidebar.children('.inner');

		// Inactive by default on <= large.
			breakpoints.on('<=large', function() {
				$sidebar.addClass('inactive');
			});

			breakpoints.on('>large', function() {
				$sidebar.removeClass('inactive');
			});

		// Hack: Workaround for Chrome/Android scrollbar position bug.
			if (browser.os == 'android'
			&&	browser.name == 'chrome')
				$('<style>#sidebar .inner::-webkit-scrollbar { display: none; }</style>')
					.appendTo($head);

		// Toggle.
			$('<a href="#sidebar" class="toggle">Toggle</a>')
				.appendTo($sidebar)
				.on('click', function(event) {

					// Prevent default.
						event.preventDefault();
						event.stopPropagation();

					// Toggle.
						$sidebar.toggleClass('inactive');

				});

		// Events.

			// Link clicks.
				$sidebar.on('click', 'a', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Vars.
						var $a = $(this),
							href = $a.attr('href'),
							target = $a.attr('target');

					// Prevent default.
						event.preventDefault();
						event.stopPropagation();

					// Check URL.
						if (!href || href == '#' || href == '')
							return;

					// Hide sidebar.
						$sidebar.addClass('inactive');

					// Redirect to href.
						setTimeout(function() {

							if (target == '_blank')
								window.open(href);
							else
								window.location.href = href;

						}, 500);

				});

			// Prevent certain events inside the panel from bubbling.
				$sidebar.on('click touchend touchstart touchmove', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Prevent propagation.
						event.stopPropagation();

				});

			// Hide panel on body click/tap.
				$body.on('click touchend', function(event) {

					// >large? Bail.
						if (breakpoints.active('>large'))
							return;

					// Deactivate.
						$sidebar.addClass('inactive');

				});

		// Scroll lock.
		// Note: If you do anything to change the height of the sidebar's content, be sure to
		// trigger 'resize.sidebar-lock' on $window so stuff doesn't get out of sync.

			$window.on('load.sidebar-lock', function() {

				var sh, wh, st;

				// Reset scroll position to 0 if it's 1.
					if ($window.scrollTop() == 1)
						$window.scrollTop(0);

				$window
					.on('scroll.sidebar-lock', function() {

						var x, y;

						// <=large? Bail.
							if (breakpoints.active('<=large')) {

								$sidebar_inner
									.data('locked', 0)
									.css('position', '')
									.css('top', '');

								return;

							}

						// Calculate positions.
							x = Math.max(sh - wh, 0);
							y = Math.max(0, $window.scrollTop() - x);

						// Lock/unlock.
							if ($sidebar_inner.data('locked') == 1) {

								if (y <= 0)
									$sidebar_inner
										.data('locked', 0)
										.css('position', '')
										.css('top', '');
								else
									$sidebar_inner
										.css('top', -1 * x);

							}
							else {

								if (y > 0)
									$sidebar_inner
										.data('locked', 1)
										.css('position', 'fixed')
										.css('top', -1 * x);

							}

					})
					.on('resize.sidebar-lock', function() {

						// Calculate heights.
							wh = $window.height();
							sh = $sidebar_inner.outerHeight() + 30;

						// Trigger scroll.
							$window.trigger('scroll.sidebar-lock');

					})
					.trigger('resize.sidebar-lock');

				});

	// Menu.
		var $menu = $('#menu'),
			$menu_openers = $menu.children('ul').find('.opener');

		// Openers.
			$menu_openers.each(function() {

				var $this = $(this);

				$this.on('click', function(event) {

					// Prevent default.
						event.preventDefault();

					// Toggle.
						$menu_openers.not($this).removeClass('active');
						$this.toggleClass('active');

					// Trigger resize (sidebar lock).
						$window.triggerHandler('resize.sidebar-lock');

				});

			});

})(jQuery);


shelf_data = {}

function refresh_data() {
	fetch('/static/database.json')
		.then((response) => {
			return response.json();
		}).then((text) => {
			console.log('Sentiment response: ' + text);
			console.log(text)

			products = {}
			for (let date in text) {
				let dataPoint = text[date]
				for (let index in dataPoint) {
					product = dataPoint[index].name;
					amount = dataPoint[index].amount;
					if (!(product in products)) {
						products[product] = []
					}
					point = {
						date: date,
						amount: amount
					}
					products[product].push(point)
				}
			}
			console.log(products)


			shelf_data = products
			updateInterface()
		});
}

function updateInterface() {
	let select_form = document.getElementById('select-products')
	console.log(select_form.innerHTML)
	let checkboxHtml = '<label>Shelf graphs</label>'
	for (let productName in shelf_data) {
		let item = `<input name="${productName}" type="checkbox"/>\n<label>${productName}</label>\n`
		checkboxHtml += item

		let product = shelf_data[productName]

	}

	select_form.innerHTML = checkboxHtml


}

// function DtoS(datetime, with_year=false) {
// 	let day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][datetime.getDay()];
// 	let month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][datetime.getMonth()];
// 	let date = datetime.getDate();


// 	return day + ' ' + date + ' ' + month + (with_year ? ' \'' + (datetime.getYear() % 100) : '');
// }

// function dateAfterNDays(n) {
// 	var date = new Date();
// 	return new Date(date.setDate(date.getDate() + n));
// }

// function updatePredictionChart() {
// 	const today = new Date();

// 	fetch('/api/get_predicted_data') .then((response) => {
// 		return response.json();
// 	}).then((text) => {
// 		console.log('Prediction response:');
// 		console.log(text);

// 		x_labels = []
// 		for (let x = 0 ; text < x.x ; length++) {
// 			x_labels.push(DtoS(dateAfterNDays(1 + x), true))
// 		}

// 		let chartData = {
// 			type: 'area',
// 			scaleX: {
// 				label: { text: "Day" },
// 				labels: x_labels
// 			},
// 			scaleY: {
// 				label: { text: "ETS Price (EUR per tonne)" }
// 			},
// 			series: [
// 				{
// 					values: text
// 				}
// 			]
// 		};

// 		zingchart.render({
// 			id: 'predictionChart',
// 			data: chartData,
// 			height: 400,
// 			width: '100%'
// 		});
// 	});
// }

// function updateHistoricalChart() {
// 	const today = new Date();

//     fetch('/api/get_historical_data') .then((response) => {
// 		return response.json();
// 	}).then((text) => {
// 		console.log('Historical response:');
// 		console.log(text);

// 		let today = new Date();
// 		x_labels = []
// 		for (let x = 0 ; x < text.length ; x++) {
// 			x_labels.push(DtoS(dateAfterNDays(x - text.length), true))
// 		}

// 		let chartData = {
// 			type: 'area',
// 			scaleX: {
// 				label: { text: "Day" },
// 				labels: x_labels
// 			},
// 			scaleY: {
// 				label: { text: "ETS Price (EUR per tonne)" }
// 			},
// 			series: [
// 				{
// 					values: text
// 				}
// 			]
// 		};

// 		zingchart.render({
// 			id: 'historicalChart',
// 			data: chartData,
// 			height: 400,
// 			width: '100%'
// 		});
// 	});
// }


function refresh() {
	refresh_data();
	// updatePredictionChart();
	// updateHistoricalChart();
}


window.onload = function() {
	refresh();
	seconds = 10
	setInterval(refresh, seconds * 1000)
	// document.find_element_by_id('refresh').on('click', (e) => {
	// 	refresh();
	// });
}

// function submitForm() {

// 	let array = $('#weatherform').serializeArray().map(x => x.value)
// 	let url = '/api/electricity_predict/' + array

// 	fetch(url).then((response) => {
// 		return response.json();
// 	}).then((text) => {
// 		let final_text = 'Predicted Electricity Consumption: ' + text + " MW"
// 		console.log(final_text)
// 		document.getElementById('predictedElectricityConsumption').innerHTML = final_text
// 	})
// }

// Render Method[3]
