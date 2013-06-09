jq(document).ready(function() {
    jq('.cmrs-news img, .portlet-image img')
        .prepOverlay({
            subtype: 'image',
            urlmatch: '/image_.+$',
            urlreplace: '/image_large'
        });
});

jq(document).ready(function() {
	$(".collapsedHeading.collapsed").next().hide();
 
	$(".collapsedHeading").click(function() {
	  $(this).next().slideToggle("fast");
	  $(this).toggleClass("collapsed");
	});
});
