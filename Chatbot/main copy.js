(function() {
    var Message, url;
    Message = function(arg) {
        (this.text = arg.text), (this.message_side = arg.message_side);
        this.draw = (function(_this) {
            return function() {
                var $message;
                $message = $(
                    $('.message_template')
                        .clone()
                        .html()
                );

                $message
                    .addClass(_this.message_side)
                    .find('.text')
                    .html(_this.text);

                if (this.message_side === 'left') {
                    url = '/static/images/bot.png';
                } else {
                    url = '/static/images/user.png';
                }
                $message
                    .find('.avatar')
                    .css('background-image', 'url(' + url + ')');
                $('.messages').append($message);
                return setTimeout(function() {
                    return $message.addClass('appeared');
                }, 0);
            };
        })(this);
        return this;
    };

    $(function() {
        var getMessageText, sendMessage;

        getMessageText = function() {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

        sendMessage = function(text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');

            message = new Message({
                text: text,
                message_side: 'right'
            });
            message.draw();

            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:5000/get',
                success: function(msg) {
                    console.log(msg.message)
                    var messages_list = msg.message;
                        message = new Message({
                            text: messages_list,
                            message_side: 'left'
                        });
                        message.draw();
                    $messages.stop().animate(
                        { scrollTop: $messages.prop('scrollHeight') },
                        700
                    );
                },
                error: function(xhr, status, error) {
                    console.error("AJAX request failed:", status, error);
                }
            });
        };

        $('.send_message').click(function() {
            return sendMessage(getMessageText());
        });

        $('.message_input').keyup(function(e) {
            if (e.which === 13) {
                return sendMessage(getMessageText());
            }
        });

        var message_greetings = new Message({
            text: 'Hi, I am LegaLifeline AI bot. How can I help you?',
            message_side: 'left'
        });
        message_greetings.draw();
    });
}.call(this));
