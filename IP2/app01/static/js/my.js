function set_menu_active() {
    var menu_id = url_spe_str_replace(window.location.pathname);
    // var menu_id = url_spe_str_replace(window.location.pathname + window.location.search);
    menu_id = $("#menu_" + menu_id);
    var menu_parent = menu_id.parent().parent();
    if(menu_parent.hasClass("sidebar-nav-sub")){
        //menu_id是二级菜单
        menu_parent.css('display','block');
        menu_parent.parent().children('#menu_').addClass('active');
        menu_parent.parent().children('#menu_').children('span').addClass('sidebar-nav-sub-ico-rotate');
        menu_id.addClass('sub-active');
    }else{
        //menu_id是一级菜单
        menu_id.addClass('active');
    }
}

function url_spe_str_replace(str) {
    var reg = /\?/g;
    var str2 = str.replace(reg,'a');
    reg = /=/g;
    str2 = str2.replace(reg,'a');
    reg = /\//g;
    str2 = str2.replace(reg,'a');
    return str2;
}
set_menu_active();