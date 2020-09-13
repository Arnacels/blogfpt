(function($) {
    // your code, use `$` as normal
    $('.like').click(function() {
                var id = window.location.pathname.split('/')[2]
                $.get('/like-post/'+id+'/').done(function( data ) {
                        console.log(data)
                        $('.like').html('Like '+data);

                    });


                });


})(window.jQuery);