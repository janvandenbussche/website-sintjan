window.sj = window.sj || {};

sj.init = function()
{
    sj.initMessage();
};

sj.moreDefaults = {
		url:'/foo/bar',
		param:'id',
		moreId:-1		
};

sj.more = function(options)
{
	var conf = $.extend({}, sj.moreDefaults, options);
	var last = $('[moreTarget='+conf.moreId+'] [moreItem]:last');
	var lastId = $(last).attr('moreItem');
	//alert("item = " + lastId);
	
	$('[moreBtn='+conf.moreId+'] a').hide().blur();
	$('[moreBtn='+conf.moreId+'] p').show();

	var url = conf.url + '?' + conf.param + "=" + lastId;
	
	$.get(url,function(data){
		$(last).after(data);
		$('[moreBtn='+conf.moreId+'] a').show();
		$('[moreBtn='+conf.moreId+'] p').hide();
	});
};


sj.initMessage = function()
{
    var msg = $('#message');

    if(msg)
    {
        msg.click(function()
        {
            $(this).fadeOut('slow');
        });

        setTimeout("$('#message').fadeOut('slow');", 3000);
    }
};



