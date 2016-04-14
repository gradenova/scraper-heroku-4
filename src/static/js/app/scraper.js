(function($, doc) {
    'use strict';

    var condition = 'open';

    doc.addEventListener('DOMContentLoaded', function() {
        initializeForm();
        initializeButton();
    });

    function initializeForm() {
        $('form.scrape').on('submit', function() {
            var $form = $(this);
            var $result = $('textarea.result');
            var urls = $('#urls').val().split(/\r\n|\r|\n/);

            prepareFetching();

            var results = _.map(urls, function(url) {
                var deferred = $.Deferred();

                $.ajax({
                    type: $form.attr('method'),
                    url: $form.attr('action'),
                    data: $form.serialize() + '&base_url=' + url,
                }).done(function(data) {
                    $result.val($result.val() + data + '\n');
                    deferred.resolve();
                }).fail(function(xhr, status, error) {
                    $result.val(error.message);
                    deferred.reject();
                });

                return deferred.promise();
            });

            closeFetching(results);

            return false;
        });
    }

    function prepareFetching() {
        $('textarea.result').val('');
        $('#loading').show();
        toggleForm();
    }

    function closeFetching(results) {
        $.when.apply(null, results).done(function() {
            $('#loading').hide();
        }).fail(function() {
            $('#loading').hide();
        });
    }

    function toggleForm() {
        if (condition === 'open') {
            $('#forms').slideUp();
            condition = 'close';
            $('button.open').show();
        } else {
            $('#forms').slideDown();
            condition = 'open';
            $('button.open').hide();
        }
    }

    function initializeButton() {
        $('button.open').on('click', function() {
            toggleForm();

            return false;
        });
    }

})(jQuery, document)
