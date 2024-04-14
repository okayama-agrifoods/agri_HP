
// ========================
// TOPに戻るボタンがでる
// ========================
$(function(){

  var showFlug = false;
  var topBtn = jQuery('#pagetop');
  topBtn.css('bottom', '-400px');
  var showFlug = false;
  var winW = $(window).width();
  var devW = 480;
  jQuery(window).scroll(function () {
    if (jQuery(this).scrollTop() > 300) {
      if (showFlug == false) {
        showFlug = true;
        if (winW <= devW) {
          topBtn.stop().animate({'bottom' : '70px'}, 1000); //以下の時の処理
          } else {
          topBtn.stop().animate({'bottom' : '30px'}, 1000); //大きい時の処理
          }
      }
    } else {
      if (showFlug) {
        showFlug = false;
        topBtn.stop().animate({'bottom' : '-500px'}, 1000); 
      }
    }
  });
  topBtn.click(function () {
    jQuery('body,html').animate({
      scrollTop: 0
    }, 400);
    return false;
  });
});

// ========================
// ページ外からのアンカーリンクもスムーズスクロールにする
// ========================
var headerHeight = $('header').outerHeight();
var urlHash = location.hash;
if(urlHash) {
    $('body,html').stop().scrollTop(0);
    setTimeout(function(){
        var target = $(urlHash);
        var position = target.offset().top - headerHeight;
        $('body,html').stop().animate({scrollTop:position}, 500);
    }, 100);
}
$(function(){
    $('a[href*="#"], area[href*="#"]').not(".noScroll").click(function() {
        var speed = 400,
						href = $(this).prop("href"),
            hrefPageUrl = href.split("#")[0],
            currentUrl = location.href,
            currentUrl = currentUrl.split("#")[0];
        if(hrefPageUrl == currentUrl){
            href = href.split("#");
            href = href.pop();
            href = "#" + href;
            var target = $(href == "#" || href == "" ? 'html' : href),
                position = target.offset().top - headerHeight;
               $('body,html').stop().animate({scrollTop:position}, 500);
            return false;
        }
    });
});

// ========================
// ハンバーガーメニュー
// ========================
$(function() {
	$('.menu-trigger').on('click',function(){
    if($(this).hasClass('active')){
      $(this).removeClass('active');
      $('main').removeClass('open');
      $('nav').removeClass('open');
      $('.overlay').removeClass('open');
    } else {
      $(this).addClass('active');
      $('main').addClass('open');
      $('nav').addClass('open');
      $('.overlay').addClass('open');
    }
  });
	$('nav, nav ul li a').on('click',function(){
    if($(this).parents("nav").hasClass('open')){
      $(this).parents("nav").removeClass('open');
      $('.menu-trigger').removeClass('active');
			$('.overlay').removeClass('open');  
    }
  });
  $('.overlay').on('click',function(){
    if($(this).hasClass('open')){
      $(this).removeClass('open');
      $('.menu-trigger').removeClass('active');
      $('main').removeClass('open');
      $('nav').removeClass('open');
			$('.overlay').removeClass('open');  
    }
  });
});


// ========================
// header アコーディオン
// ========================

//読み込み時
$(function(){
    $('.accTitle').click(function(event){
        $(this).siblings('.accInner').slideToggle();
        $('.accTitle').not($(this)).siblings('.accInner').slideUp();
        $('.accTitle').not($(this)).removeClass("accOn");
        $(this).toggleClass("accOn");
        // ウィンドウの中身をクリックしても、閉じないようにする
        // (親要素への伝播を止める)
        event.stopPropagation();
    });
});



