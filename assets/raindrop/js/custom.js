// csrf
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

// продажа вещи пользователя купленной в магазине
function sell_stuff_shop(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/shop/sell_stuff',
        data: {
            'stuff_id': stuff_id
        },
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#stuff" + stuff_id).remove();
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Вещь размещена в магазине успешно!');
                $("#stuff-shop-" + stuff_id).remove();
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка размещения вещи в магазине. У вас не хватает монет.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    $('#modal-payment').modal({
                        backdrop: 'static',
                        keyboard: false
                    });
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// снятие вещи с продажи
function remove_sell_stuff_shop(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/shop/remove_sell_stuff',
        data: {
            'stuff_id': stuff_id
        },
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#stuff" + stuff_id).remove();
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Вещь снята с продажи!');
                $("#stuff-shop-" + stuff_id).remove();
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка снятия вещи с продажи.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    $('#modal-payment').modal({
                        backdrop: 'static',
                        keyboard: false
                    });
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// продажа вещи пользователя купленной в магазине
function sell_stuff_games(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/lottery/sell_stuff',
        data: {
            'stuff_id': stuff_id
        },
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#stuff" + stuff_id).remove();
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Вещь размещена в магазине успешно!');
                $("#stuff-shop-" + stuff_id).remove();
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка размещения вещи в магазине. У вас не хватает монет.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    $('#modal-payment').modal({
                        backdrop: 'static',
                        keyboard: false
                    });
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// покупка вещи в магазине
function payment_shop(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/shop/payment',
        data: 'stuff_id=' + stuff_id,
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#stuff" + stuff_id).remove();
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Покупка произведена успешно!');
                $("#stuff-shop-" + stuff_id).remove();
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка покуки. У вас не хватает монет.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    $('#modal-payment').modal({
                        backdrop: 'static',
                        keyboard: false
                    });
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// добавление вещи в избранное
function favorites_shop(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/shop/favorites',
        data: 'stuff_id=' + stuff_id,
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Вещь добавлена в избранное.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Вещь не добавлена в избранное. Внутренняя ошибка.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// удаление вещи из избранного
function favorites_remove_shop(stuff_id) {
    $.ajax({
        type: 'POST',
        url: '/shop/favorites_remove',
        data: {
            'stuff_id': stuff_id
        },
        success: function (data) {
            data = JSON.parse(data);
            if (data.status === "success") {
                $("#stuff" + stuff_id).remove();
                $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Вещь удаления из избранного.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-success').css({display: "none"});
                }, 2000);
            } else if (data.status === "fail") {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Вещь не удалена из избранного. Внутренняя ошибка.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        },
        error: function () {
            $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
            setTimeout(function () {
                $("#rd-alert").removeClass('alert-danger').css({display: "none"});
            }, 2000);
        }
    });
    return false;
}

// показ модального окна после выгрыша в режиме dotabox
function choose_dotabox(id, type) {
    $("#dotabox-case" + id).animate({"top": "-=30px"}, "fast");
    $("#dotabox-case-score" + id).text(id + ' монет');

    setTimeout(function () {
        if (type === 0) {
            $('#dotabox-modal').modal({
                backdrop: 'static',
                keyboard: false
            })
        } else if (type === 1) {
            $('#dotabox-free-modal').modal({
                backdrop: 'static',
                keyboard: false
            })
        }
    }, 1000);

    return false;
}

// показ модального окна авторизации
function show_auth_modal() {
    $('#auth-modal').modal({
        backdrop: 'static',
        keyboard: false
    });
}

$(document).ready(function () {
    var dotabox_case1 = $('#dotabox-case1');
    var dotabox_case2 = $('#dotabox-case2');
    var dotabox_case3 = $('#dotabox-case3');
    var dotabox_case4 = $('#dotabox-case4');

    // подсветка активной ссылки в главном меню
    $("#header_navigation").find("li a").each(function () {
        var location = window.location.href.split('/')[3];
        var link = this.href.split('/')[3];
        if (location === link) {
            $(this).parent().addClass("active");
        }
    });

    // подсветка активной ссылки в личном кабинете пользователя
    $("#profile_navigation").find("li a").each(function () {
        var location = window.location.href;
        var link = this.href;
        if (location === link) {
            $(this).parent().addClass("df-account-navigation__link--active");
        }
    });

    // подсветка активной ссылки в режиме dotabox
    $("#dotabox-nav").find("li a").each(function () {
        var location = window.location.href;
        var link = this.href;
        if (location === link) {
            $(this).parent().addClass("content-filter__item--active");
        }
    });

    // отправка почты
    $("#contact-form").submit(function () {
        $.ajax({
            type: $("#contact-form").attr("method"),
            url: $("#contact-form").attr("action"),
            data: $("#contact-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Ваше письмо успешно отправлено!');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-success').css({display: "none"});
                    }, 2000);
                } else if (data.status === "fail") {
                    $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Письмо не было отправлено. Внутренняя ошибка, свяжитесь с нами лругим способом.');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    }, 2000);
                }
            },
            error: function () {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        });
        return false;
    });

    // обновление дополнительной информации о пользователе в личном кабинете
    $("#user-service-form").submit(function () {
        $.ajax({
            type: $("#user-service-form").attr("method"),
            url: $("#user-service-form").attr("action"),
            data: $("#user-service-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Профиль успешно обновлен!');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-success').css({display: "none"});
                    }, 2000);
                } else if (data.status === "fail") {
                    $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Профиль не был обновлен. Внутренняя ошибка, свяжитесь с администратором сайта.');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    }, 2000);
                }
            },
            error: function () {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        });
        return false;
    });

    // обновление информации пользователя в личном кабинете
    $("#user-form").submit(function () {
        $.ajax({
            type: $("#user-form").attr("method"),
            url: $("#user-form").attr("action"),
            data: $("#user-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    $("#rd-alert").addClass('alert-success').css({display: "block"}).html('Профиль успешно обновлен!');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-success').css({display: "none"});
                    }, 2000);
                } else if (data.status === "fail") {
                    $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Профиль не был обновлен. Внутренняя ошибка, свяжитесь с администратором сайта.');
                    setTimeout(function () {
                        $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                    }, 2000);
                }
            },
            error: function () {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        });
        return false;
    });

    // анимация и розыгрыш вещи в режиме rd case
    $('#rdcase-button').click(function () {
        $('#rdcase-button').attr("disabled", "disabled");
        $.ajax({
            type: 'POST',
            url: '/briefcases/rdcase_action/',
            data: 'id_case=' + $(this).data('rdcase'),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    for (i = 0; i < 100; i = i + 1) {
                        $('.rdcase-case-items').animate({"left": "-=10px"}, 10);
                    }
                    setTimeout(function () {
                        $('#rdcase-img').attr("src", data.content.img);
                        $('#rdcase-title').text(data.content.title);
                        $('#rdcase-score').text(data.content.score + ' монет');
                        $('#rdcase-modal').modal({
                            backdrop: 'static',
                            keyboard: false
                        });
                    }, 3000);
                } else if (data.status === "fail") {
                    $('#modal-payment').modal({
                        backdrop: 'static',
                        keyboard: false
                    });
                }
            },
            error: function () {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        });
        return false;
    });

    // анимация и розыгрыш вещи в режиме dotabox
    $("#dotabox-button").click(function () {
        $('#dotabox-button').attr("disabled", "disabled");
        $.ajax({
            type: 'POST',
            url: '/dotabox/dotabox_action/',
            data: 'id_dotabox=' + $(this).data('dotabox'),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    setTimeout(function () {
                        $(".dotabox_case").animate({"top": "-=30px"}, "fast");
                        setTimeout(function () {
                            $('#dotabox-case-score1').text(data.case_all.case1 + ' монет');
                            $('#dotabox-case-score2').text(data.case_all.case2 + ' монет');
                            $('#dotabox-case-score3').text(data.case_all.case3 + ' монет');
                            $('#dotabox-case-score4').text(data.case_all.case4 + ' монет');

                            setTimeout(function () {
                                $(".dotabox_case").animate({"top": "+=30px"}, "fast");
                                $(".dotabox_case_score").empty();

                                setTimeout(function () {
                                    $('.dotabox_case span').remove();

                                    dotabox_case2.animate({"left": "-=300px"}, "fast");
                                    dotabox_case3.animate({"left": "-=600px"}, "fast");
                                    dotabox_case4.animate({"left": "-=900px"}, "fast");

                                    setTimeout(function () {
                                        dotabox_case2.animate({"left": "+=300px"}, "fast");
                                        dotabox_case3.animate({"left": "+=600px"}, "fast");
                                        dotabox_case4.animate({"left": "+=900px"}, "fast");

                                        setTimeout(function () {
                                            dotabox_case1.animate({"left": "+=900px"}, "fast");
                                            dotabox_case4.animate({"left": "-=900px"}, "fast");

                                            dotabox_case2.animate({"left": "+=300px"}, "fast");
                                            dotabox_case3.animate({"left": "-=300px"}, "fast");

                                            setTimeout(function () {
                                                dotabox_case4.animate({"left": "+=300px"}, "fast");
                                                dotabox_case3.animate({"left": "-=300px"}, "fast");

                                                dotabox_case2.animate({"left": "+=300px"}, "fast");
                                                dotabox_case1.animate({"left": "-=300px"}, "fast");

                                                setTimeout(function () {
                                                    dotabox_case3.animate({"left": "+=300px"}, "fast");
                                                    dotabox_case4.animate({"left": "-=300px"}, "fast");
                                                    dotabox_case1.animate({"left": "+=300px"}, "fast");
                                                    dotabox_case2.animate({"left": "-=300px"}, "fast");

                                                    setTimeout(function () {
                                                        $('#dotabox-result-txt').css({display: "block"});

                                                        if (data.type_game === 'pay') {
                                                            dotabox_case1.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(1, 0)"></a>');
                                                            dotabox_case2.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(2, 0)"></a>');
                                                            dotabox_case3.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(3, 0)"></a>');
                                                            dotabox_case4.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(4, 0)"></a>');

                                                            $('#dotabox-img').empty().attr("src", data.stuff.img);
                                                            $('#dotabox-title').empty().text(data.stuff.title);
                                                            $('#dotabox-score').empty().text(data.stuff.score + ' монет');
                                                        } else if (data.type_game === 'free') {
                                                            dotabox_case1.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(1, 1)"></a>');
                                                            dotabox_case2.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(2, 1)"></a>');
                                                            dotabox_case3.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(3, 1)"></a>');
                                                            dotabox_case4.wrapAll('<a href="javascript:void(1)" onclick="choose_dotabox(4, 1)"></a>');

                                                            $('#dotabox-free-img').empty().attr("src", data.stuff.img);
                                                            $('#dotabox-free-title').empty().text(data.stuff.title);
                                                            $('#dotabox-free-score').empty().text(data.stuff.score + ' монет');
                                                        }
                                                    }, 1000);
                                                }, 1000);
                                            }, 1000);
                                        }, 1000);
                                    }, 1000);
                                }, 1000);
                            }, 2000);
                        }, 1000);
                    }, 1000);
                } else if (data.status === "fail") {
                    $('#modal-payment').modal('show');
                }
            },
            error: function () {
                $("#rd-alert").addClass('alert-danger').css({display: "block"}).html('Ошибка сервера, попробуйте еще раз.');
                setTimeout(function () {
                    $("#rd-alert").removeClass('alert-danger').css({display: "none"});
                }, 2000);
            }
        });
        return false;
    });

    // перезагрузка страницы после выигрыша вещи
    $('#reload-page-button').click(function () {
        location.reload();
    });

    $('#filter-price-form').submit(function () {
        $('#min-price-input').val(parseInt($('#slider-range-value-min').text()));
        $('#max-price-input').val(parseInt($('#slider-range-value-max').text()));
    });
});