function dateDiff(interval, date1, date2)
{
	var objInterval = {'D' : 1000 * 60 * 60 * 24, 'H' : 1000 * 60 * 60, 'M' : 1000 * 60, 'S' : 1000, 'T' : 1};
	interval = interval.toUpperCase();
	var dt1 = Date.parse(date1.replace(/-/g, '/'));
	var dt2 = Date.parse(date2.replace(/-/g, '/'));
	try
	{
		return Math.round((dt2 - dt1) / eval('(objInterval.' + interval + ')'));
	}
	catch (e)
	{
		return e.message;
	}
}
Date.prototype.pattern=function(fmt) {           
    var o = {           
    "M+" : this.getMonth()+1, //月份           
    "d+" : this.getDate(), //日           
    "h+" : this.getHours()%12 == 0 ? 12 : this.getHours()%12, //小时           
    "H+" : this.getHours(), //小时           
    "m+" : this.getMinutes(), //分           
    "s+" : this.getSeconds(), //秒           
    "q+" : Math.floor((this.getMonth()+3)/3), //季度           
    "S" : this.getMilliseconds() //毫秒           
    };           
    var week = {           
    "0" : "/u65e5",           
    "1" : "/u4e00",           
    "2" : "/u4e8c",           
    "3" : "/u4e09",           
    "4" : "/u56db",           
    "5" : "/u4e94",           
    "6" : "/u516d"          
    };           
    if(/(y+)/.test(fmt)){           
        fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));           
    }           
    if(/(E+)/.test(fmt)){           
        fmt=fmt.replace(RegExp.$1, ((RegExp.$1.length>1) ? (RegExp.$1.length>2 ? "/u661f/u671f" : "/u5468") : "")+week[this.getDay()+""]);           
    }           
    for(var k in o){           
        if(new RegExp("("+ k +")").test(fmt)){           
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));           
        }           
    }           
    return fmt;           
}         
function checkValue(value, defaultvalue) {
	defaultvalue = defaultvalue || '';
	if (value == '' || typeof(value) == 'undefined') {
		value = defaultvalue;
	}
	return value;
};     
function timer(date1,date2,isen){
	var timestatus=0;//未开始
	var date = new Date();        
	date2=checkValue(date2,'');
	if (date2==''){
		date2=date1;
	}
	isen=checkValue(isen,0);
	var msg1=isen==1?'End of the Eent':'大赛已结束'
	var msg2=isen==1?'Meeting':'大赛进行中'

	var now=date.pattern("yyyy-MM-dd hh:mm:ss");  

	var intDiff=parseInt(dateDiff('S', now,date1));
	var intDiff1=parseInt(dateDiff('S', date2, now));

	var $boxtime=$('#box-timer');
	var liveUrl=checkValue($boxtime.data('liveurl'),'');
	
	
	if (intDiff1>0){
		$('.time-item').html('<div class="time-end" style="font-size:20px;text-align:center;">'+msg1+'</div>');
		timestatus=2;//已结束
		if (liveUrl!=''){
			$('.time-item').html('<a href="'+liveUrl+'" target="_blank" class="time-end" style="font-size:20px;text-align:center;color:#0e45d4">查看回放</a>');
		}
	}
	else if(intDiff1<=0 &&intDiff<=0){
		$('.time-item').html('<div class="time-end time-ing" style="font-size:20px;text-align:center;">'+msg2+'</div>');
		timestatus=1;//进行中
		if (liveUrl!=''){
			$('.time-item').html('<a href="'+liveUrl+'" target="_blank" class="time-end  time-ing" style="font-size:20px;text-align:center;color:#f30">在线直播</a>');
		}		
	}

	else
	{
		window.setInterval(function(){
		var day=0,
			hour=0,
			minute=0,
			second=0;//时间默认值       
		if(intDiff > 0){
			day = Math.floor(intDiff / (60 * 60 * 24));
			hour = Math.floor(intDiff / (60 * 60)) - (day * 24);
			minute = Math.floor(intDiff / 60) - (day * 24 * 60) - (hour * 60);
			second = Math.floor(intDiff) - (day * 24 * 60 * 60) - (hour * 60 * 60) - (minute * 60);
		}
		if (hour <= 9) hour = '0' + hour;
		if (minute <= 9) minute = '0' + minute;
		if (second <= 9) second = '0' + second;
		if (isen==0)
		{
			$('#day_show').html(day+"<span>天</span>");
			$('#hour_show').html('<s id="h"></s>'+hour+'<span>时</span>');
			$('#minute_show').html('<s></s>'+minute+'<span>分</span>');
			$('#second_show').html('<s></s>'+second+'<span>秒</span>');
		}
		if (isen==1)
		{
			$('#day_show').html(day+"<span>D</span>");
			$('#hour_show').html('<s id="h"></s>'+hour+'<span>H</span>');
			$('#minute_show').html('<s></s>'+minute+'<span>m</span>');
			$('#second_show').html('<s></s>'+second+'<span>S</span>');
		}

		intDiff--;
		}, 1000);
	}
	return timestatus;
} 

function getChildNum(cur) {
    if (cur.children('ul').length > 0){
        var num = cur.children('ul').children().length;
    }else{
        var num = cur.children().length;
    }
    cur.parents('.box').addClass(cur.selector.substr(1) + '-' + num)
}
// 获取滚动条宽度
function getScrollbarWidth() {
    var oP = document.createElement('p'), styles = {
        width: '100px',
        height: '100px',
        overflowY: 'scroll',
    }, i, scrollbarWidth;

    for (i in styles){
        oP.style[i] = styles[i];
    }
    document.body.appendChild(oP);
    scrollbarWidth = oP.offsetWidth - oP.clientWidth;
    oP.remove();

    return scrollbarWidth;
}

//判断PC端
function isPc(){
    if ($(window).width() >= 768){
        return true;
    }
};

//判断移动端
function isMobile(){
    if ($(window).width() < 768){
        return true;
    }
};


function getUrlFileName(url){
		url=url.split('?')[0];
		var c=url.split('/').length;
		var filename=url.split('/')[c-1].toLowerCase();
		filename=url.split('#')[0];
		return filename;
};
/*------------------------------------------------------------地图*/

function createMap(x,y){
	var map = new BMap.Map("mapcontent");//在百度地图容器中创建一个地图
	var point = new BMap.Point(x,y);//定义一个中心点坐标
	map.centerAndZoom(point,17);//设定地图的中心点和坐标并将地图显示在地图容器中
	window.map = map;//将map变量存储在全局
}

//地图事件设置函数：
function setMapEvent(){
	//map.disableDragging();//启用地图拖拽事件，默认启用(可不写)
	map.disableScrollWheelZoom(true);//禁用地图滚轮放大缩小，默认禁用(可不写)
	map.enableDoubleClickZoom();//启用鼠标双击放大，默认启用(可不写)
	map.enableKeyboard();//启用键盘上下左右键移动地图
}

//地图控件添加函数：
function addMapControl(){
	//向地图中添加缩放控件
	var ctrl_nav = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_LARGE});
	map.addControl(ctrl_nav);
}


//创建marker
function addMarker(markerArr){
	for(var i=0;i<markerArr.length;i++){
		var json = markerArr[i];
		var p0 = json.point.split("|")[0];
		var p1 = json.point.split("|")[1];
		var point = new BMap.Point(p0,p1);
		var iconImg = createIcon(json.icon);
		var marker = new BMap.Marker(point,{icon:iconImg});
		var iw = createInfoWindow(i,markerArr);
		var label = new BMap.Label(json.title,{"offset":new BMap.Size(json.icon.lb-json.icon.x+10,-20)});
		marker.setLabel(label);
		map.addOverlay(marker);
		label.setStyle({
					borderColor:"#808080",
					color:"#333",
					cursor:"pointer"
		});

		(function(){
			var index = i;
			var _iw = createInfoWindow(i,markerArr);
			var _marker = marker;
			_marker.addEventListener("click",function(){
				this.openInfoWindow(_iw);
			});
			_iw.addEventListener("open",function(){
				_marker.getLabel().hide();
			})
			_iw.addEventListener("close",function(){
				_marker.getLabel().show();
			})
			label.addEventListener("click",function(){
				_marker.openInfoWindow(_iw);
			})
			if(!!json.isOpen){
				label.hide();
				_marker.openInfoWindow(_iw);
			}
		})()
	}
}
//创建InfoWindow
function createInfoWindow(i,markerArr){
	var json = markerArr[i];
	var iw = new BMap.InfoWindow("<b class='iw_poi_title' title='" + json.title + "'>" + json.title + "</b><div class='iw_poi_content'>"+json.content+"</div>");
	return iw;
}
//创建一个Icon
function createIcon(json){
	var icon = new BMap.Icon("http://map.baidu.com/image/us_mk_icon.png", new BMap.Size(json.w,json.h),{imageOffset: new BMap.Size(-json.l,-json.t),infoWindowOffset:new BMap.Size(json.lb+5,1),offset:new BMap.Size(json.x,json.h)})
	return icon;
}
/*------------------------------------------------------------地图end*/
/*------------------------------------------------------------*/

var _Guest={
    init: function() {
		//console.log('_Guest_a');
        this.swiper();
		this.click();
		this.loadMore();
    },
	/*识别嘉宾滑动*/
	swiper:function(){		
		var $swiper=$('.swiper');
		//console.log('_Guest_b');
		if($swiper.length>0){
			var $guests=$swiper.find('.guests-list');
			if ($guests.length>0){
				$guests.addClass('guests-container');
				$guests.find('ul').addClass('swiper-wrapper').after('<div class="swiper-button-next"></div><div class="swiper-button-prev"></div>');
				$guests.find('li').addClass('swiper-slide');
				//嘉宾轮播
				var swiper = new Swiper('.guests-container', {
					slidesPerView: 5,
					slidesPerGroup: 5,
					slidesPerColumn: 2,
					slidesPerColumnFill : 'row',
					spaceBetween: 30,
					navigation: {
						nextEl: '.swiper-button-next',
						prevEl: '.swiper-button-prev'
					}
				});
			}
		}	
	},
	/*嘉宾点击*/
	click:function(){
		$('.guests-list ul li').click(function () {
			var url=$(this).data("href");
			if (url==''){
				return;
			}
			$.ajax({
				type:"get",
				url: $(this).data("href"), //需要获取的页面内容
				async:true,
				success:function(data){
					var idx = 0;
	       var did = data['data'][idx].id;
         var name = data['data'][idx].name;
         var job = data['data'][idx].job;
         var avatar = data['data'][idx].avatar;
         var desc = data['data'][idx].introduction;
					var datactx = '<div class="peopleshow"><div class="peopleimg"><div><img src="'+avatar+'" alt="'+name+'"></div></div><div class="peopleinfo"><div class="peoplename">'+name+'</div><div class="peoplejob">'+job+'</div><div class="peopledes">'+desc+'</div></div></div>';					
				layer.open({
					type: 1,
					area: ["600px", "500px"],
					offset: 'auto',
					skin: 'layer-guests',
					title: false,
					scrollbar: false,
					closeBtn: 0,
					shadeClose: true,
					shade: 0.8,
					content: datactx
				})
				}
			});			
		});	
	},
	loadMore:function(){
		var $ld=$('.box-group .loadmore .guests-list');
		if ($ld.length>0){
			var $li=$ld.find('li');
			if($li.length>0){
				var h=$li.eq(0).height();
				var defaultUrl='javascript:void(0);';
				var moreurl=checkValue($ld.closest('.box-slicestyle').data('moreurl'),defaultUrl);
				$ld.find('ul').css({'height':(2*h+40)+'px','overflow':'hidden'});
				var $btn=$ld.find('.btn-loadmore');
				if($btn.length<1){
					$ld.append('<div class="box-loadmore guests-loadmore"><a href="'+moreurl+'" class="btn btn-loadmore">查看更多</a></div>');
					if (moreurl==defaultUrl){
						$btn=$ld.find('.btn-loadmore');
						$btn.click(function(){
							$ld.find('ul').css({'height':'auto'});
							$ld.find('.box-loadmore').hide();
						});
					}
				}
			}
		}
	}
};
var _Media={
	init:function(){
		this.click();
		$('.media-list ul li .facylink').each(function(){
			var url=$(this).attr('href');
			$(this).attr('href','javascript:void(0);').attr('data-href',url);
		});
	},
	/*嘉宾点击*/
	click:function(){
		$('.media-list ul li').click(function () {
			var url=checkValue($(this).data("href"),'');
			if (url==''){
				return;
			}			
			$.ajax({
				type:"get",
				url: $(this).data("href"), //需要获取的页面内容
				async:true,
				success:function(data){
				layer.open({
					type: 1,
					area: ["600px", "500px"],
					offset: 'auto',
					skin: 'layer-media',
					title: false,
					scrollbar: false,
					closeBtn: 0,
					shadeClose: true,
					shade: 0.8,
					content: data
				})
				}
			});			
		});	
	},
};
/*------------------------------------------------------------*/
var _Web={
    init: function() {
		//解决移动端点击300ms延迟
		if(isMobile()){
			FastClick.attach(document.body);
		};
	
		/*切入动画*/
		$('.box_content').waypoint(function(direction) {
			$('.box_content').addClass('animationViewWrap');
		}, {
			offset: function() {
				return window.innerHeight*.8
			}
		});
		
		/*点击向上*/
		jQuery(".box-scoll .weixin-icon").mouseenter(function(){
			$(this).find('.showimg').show().stop().animate({opacity: '1'}, 300);
		}).mouseleave(function(){
			$(this).find('.showimg').hide().stop().animate({opacity: '0'}, 200);
		});

		jQuery(".box-scoll .totop-icon").click(function(e){
			e.preventDefault();
			jQuery("html, body").animate({ scrollTop: 0 }, "slow");
			return false;
		});

		/*左右高度一致*/
		var $bel=$('.box-equal').find('.box-l');
		var $ber=$('.box-equal').find('.box-r');
		if($bel.height()<$ber.height()){
			$bel.height($ber.height());
		}
		else{
			$ber.height($bel.height());
		}
	
		this.lazyLoad();
		this.scollFixedHeader();
		this.bannerSwiper();
		this.baiduMap();	
		this.newsSwiper();
		this.loadTimer();
		this.showLiveUrl();
		this.menuUrl();
		this.mobile();
		this.boxTabs();
    },
	boxTabs:function(){
		/*切换标签*/
		$('.box-tabs .tab-nav li').click(function () {
			var cur = $(this), tabul = cur.parent(), cont =cur.parents('.box-tabs').next(), i = tabul.children().index(cur);
			if(cur.parents('.box-tabs').parents('.v50-agenda')){
				if(cur.hasClass('on')){
					cur.removeClass('on');
					cont.children().eq(i).addClass('hide');
				}else{
					$('.v50-agenda').find('.tab-nav').children().removeClass('on');
					$('.v50-agenda').find('.tab-content').children('.agenda-item').addClass('hide');
					cont.children().addClass('hide');
					tabul.children().removeClass('on');
					cur.addClass('on');
					cont.children().eq(i).removeClass('hide');
				}
			}else{
				tabul.children().removeClass('on');
				cur.addClass('on');
				cont.children().addClass('hide');
				cont.children().eq(i).removeClass('hide');
			}
		});
	},
	/*识别banner滑动*/
	bannerSwiper:function(){
		var $banner=$('#banner');
		var $swiper=$('#banner');//$banner.find('.swiper');
		if($swiper.length>0){
			var $list=$swiper.find('li');
			if ($list.length>1){
				//$swiper.addClass('swiper-container');
				$swiper.find('ul').addClass('swiper-wrapper').after('<div class="swiper-pagination"></div>');
				$swiper.find('li').addClass('swiper-slide');
				//播放
				var swiper = new Swiper('.swiper-container', {
					direction:'horizontal',
					autoplay: {
					delay: 6000,
					stopOnLastSlide: false,
					disableOnInteraction: true,
					},//--每秒中轮播一次
                    loop:true,//--可以让图片循环轮播
                    pagination:{el: '.swiper-pagination', clickable:true},//--让小圆点显示
　　　　　　　　　　effect:"fade"//--可以实现3D效果的轮播
				});
			}
		}	
	},
		/*固定导航菜单*/
	scollFixedHeader:function(){
		// 导航固定
		$(document).scroll(function () {
			var height = $(".box-group").eq(0).offset().top - $(window).scrollTop() - 60;
			////console.log(height);
			if (height <= 0) {
			  $(".header").addClass('header-fixed');
			}
			else {
			  $(".header").removeClass('header-fixed');
			}
		});	
	},
		//地图显示
	baiduMap:function(){	
		var $mapcontent=$('#mapcontent');
		if ($mapcontent.length>0){			
			var cols=$mapcontent.data('cols');
			var pointx=$mapcontent.data('pointx');
			var pointy=$mapcontent.data('pointy');
			if (cols<=1){
				$mapcontent.closest('.main').removeClass('main');
			}
			var markerArr = [{title:""+$mapcontent.data('title')+"",content:""+$mapcontent.data('address')+"",point:""+pointx+"|"+pointy+"",isOpen:1,icon:{w:23,h:25,l:23,t:21,x:9,lb:12}}];			
			createMap(pointx,pointy);//创建地图
			setMapEvent();//设置地图事件
			addMapControl();//向地图添加控件
			addMarker(markerArr);//向地图中添加marker
		}		
	},
		/*懒加载*/
	lazyLoad:function(){
		if (!jQuery().lazyload) {return;};
		$('.media-list').find("img").lazyload({placeholder: "https://pic2.pedaily.cn/19/201903/20190319@361929.png"});
		$('.guests-list').find("img").lazyload({placeholder: "https://pic2.pedaily.cn/19/201903/20190319@361931.png"});
		$('.news-list').find("img").lazyload({placeholder: "https://static.pedaily.cn/head/css/images/noimage.png"});
	},
		/*新闻轮播*/
	newsSwiper:function(){
		var swiper = new Swiper('.news-swiper',{
				autoplay:5000,
				speed:600,
				autoplayDisableOnInteraction : false,
				loop:true,
				centeredSlides : true,
				slidesPerView:2,
			navigation: {
				nextEl: '.swiper-button-next',
				prevEl: '.swiper-button-prev',
			},
				onInit:function(swiper){
					swiper.slides[2].className="swiper-slide swiper-slide-active";//第一次打开不要动画
				},
			breakpoints: {
				668: {
					slidesPerView: 1,
				}
			}
		});		
	},
	loadTimer:function(){
		var $t=$('#time_item');
		if ($t.length>0){
			var date1=$t.data('date');
			var date2=$t.data('enddate');
			var isen=checkValue($t.data('isen'),0);
			var tstatus=timer(date1,date2,isen);

			
		}
	},
	showLiveUrl:function(){
		//this.loadTimer();
		
		
	},
	/*处理菜单url的锚点链接*/
	menuUrl:function(){
		var url=window.location.href;
		if(url.indexOf('.asp')<0){
			var filename=getUrlFileName(url);
			if (filename.indexOf('index.shtml')<=-1||filename.indexOf('home.shtml')<=-1){
				$('#menulist').find('a').each(function(){
					var thisurl=$(this).attr('href');
					var fn=getUrlFileName(thisurl);
					if(thisurl.indexOf('http://')>-1||thisurl.indexOf('https://')>-1){
						
					}else{
						if (fn!='index.shtml'||fn!='home.shtml'){
							$(this).attr('href','./'+thisurl);
						}
					}
				});
			}
		}		
	},
	mobile:function(){
		if(isMobile()){
			var menu = $(".header");
			menu.addClass("mobile-menu");
			menu.prepend('<div class="hamburger" id="hamburger-11"><span class="line"></span><span class="line"></span><span class="line"></span></div>');
			$(".hamburger").click(function(e){
				e.stopPropagation();
				e.preventDefault();
				$(this).toggleClass("is-active");
				$('ul.menulist').toggleClass("flex")
				$('body').toggleClass("overflow_hidden")
			});
				/*处理菜单*/
			$('.menulist li a').click(function(){
				$('.hamburger').toggleClass("is-active");
				$('body').toggleClass("overflow_hidden");
				$(this).closest('.menulist').removeClass('flex');	
			});
			/*去掉多个换行*/
			$('.editarea').each(function(){
				var html=$(this).html();
				html=html.replace('<br><br>','')
				html=html.replace('<br/><br/>','')
				html=html.replace(/<br>(\s*\n*\r*)?<br>/ig,'')
				$(this).html(html);
			});
			/*处理议程*/
			var $agenda=$('.box_agenda');
			if($agenda.find(".agenda-item").length > 1){
                $agenda.find('.agenda-item').removeClass('hide');
			    $agenda.find('.agenda-item').find('ul').slideUp();
				$agenda.find('.agenda-item').each(function(index){
					var $s=$(this).closest('.box_agenda').find('.tab-nav li').eq(index).clone();
					var $t=$('<div class="tab-nav tab-li"></div>');

					$t.append($s);
					$(this).prepend($t);
					//$(this).slideDown();
					if(index==0){
						$(this).find('ul').slideDown();
					}
				}).click(function(){
					$(this).closest('.box_agenda').find('.agenda-item ul').slideUp();
					$(this).find('ul').slideDown();		

					$(this).closest('.box_agenda').find('.tab-li li').removeClass('on');
					$(this).find('.tab-li li').addClass('on');
				
				});
			}else{
                $agenda.find('.agenda-item ul').slideDown();
            };
		}
	}
};

var _Form={
	init:function(){
	   if ($.validator) {
			$.validator.adderror = function(element, errorcontent) {
				$(".submit").attr("disabled", "disabled");
				$.validator.clean();
				var formgroup = element.closest(".form-group");
				formgroup.addClass("has-error");
				layer.msg(errorcontent, function() { $(".submit").removeAttr("disabled"); });
			};
		};
		$('#register-form').validate({
            btnmsg: '请稍候...',
           ShowProgress: false,
            showerror: false,
            showallerror: false,
            showErrormsg: false,
            aftersubmit: function(data) {
                layer.msg(data);
            }
        });
	},
};
jQuery.validator.addMethod("checkValidcode",
	function(value, element, param, error, cannull) {
		var data = "&code=" + value;
		var flag = false;
		$.ajax({
			type: "post",
			async: false,
			cache: false,
			url: "/handler.aspx?action=checkvcode",
			data: data,
			success: function(result) {
				if (result) {
					if (result.code == 1) {
						flag = true;
					} else {
						$("#register-form #loginvcodeimg").click();
					}
				}
			},
			error: function() { flag = false; },
			dataType: "json"
		});
		return flag;
});

/*------------------------------------------------------------*/

$(function () {
	_Web.init(); 
	_Guest.init();
	_Media.init();
	_Form.init();
	var $img=$('#register-form #loginvcodeimg');
	if($img.length>0){
		$img.click(function () { this.src = '/handlers/vcode.ashx?t=' + new Date().getTime(); });
        $img.click();
	}
});
