//<script type="text/javascript" language="javascript" src="https://res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>
var url = location.href.split("#")[0];
var title=$('#box-copyright').data('title');
var desc=$('#box-copyright').data('desc');
var link=$('#box-copyright').data('link');
var imgurl=$('#box-copyright').data('imgurl');
if(!title || title.length<1){
	title= document.title;
}
if(!desc || desc.length<1){
	desc= $("#eventssharecontent").html();
}
if(!link || link.length<1){
	link= url;
}
if(!imgurl || imgurl.length<1){
	imgurl=  "http://pic2.pedaily.cn/201701/20170118110936853685.jpg";
}
var newsdata = {
    title: title,
    desc: desc,
    link: link,
    imgurl: imgurl
};
 var url = location.href.split("#")[0];
var t = 0;
if (url.indexOf('www.ghctc.com.cn') > 0) {
	t = 2;
}
$.ajax({
    url: "/top/handlers/weixin.ashx?action=config&t="+t,
    type: "post",
    data: { url: encodeURIComponent(url)},
    success: function (data) {
        if (data.code === 1) {
            wx.config({
                debug: false,
                appId: data.data.appid,
                timestamp: data.data.timestamp,
                nonceStr: data.data.nonceStr,
                signature: data.data.signature,
                jsApiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone"]
            });

        }
    }
});wx.ready(function () {
    wx.onMenuShareAppMessage({
        title: newsdata.title,
        desc: newsdata.desc, 
        link: newsdata.link,
        imgUrl: newsdata.imgurl,
        type: "link", 
        dataUrl: "", 
        success: function () {},
        cancel: function () {}
    });
    wx.onMenuShareTimeline({
        title: newsdata.title,
        link: newsdata.link,
        imgUrl: newsdata.imgurl,
        success: function () {},
        cancel: function () {}
    });
    wx.onMenuShareQQ({
        title: newsdata.title,
        desc: newsdata.desc,
        link: newsdata.link,
        imgUrl: newsdata.imgurl,
        success: function () { },
        cancel: function () { }
    });
    wx.onMenuShareWeibo({
        title: newsdata.title,
        link: newsdata.link,
        imgUrl: newsdata.imgurl,
        success: function () { },
        cancel: function () { }
    });
    wx.onMenuShareQZone({
        title: newsdata.title,
        link: newsdata.link,
        imgUrl: newsdata.imgurl,
        success: function () { },
        cancel: function () { }
    });
});