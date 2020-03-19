// var csrftoken = Cookies.get('csrftoken');
//
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
//
// $.ajaxSetup({
//     beforeSend: function (xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });
//
// $(document).ready(function () {
//     $('a.vote').click(function (e) {
//         e.preventDefault();
//         $.post('{% url "bug_vote" %}',
//             {
//                 id: $(this).data('id'),
//                 action: $(this).data('action')
//             },
//             function (data) {
//                 if (data['status'] === 'ok') {
//                     var previous_action = $('a.vote').data('action');
//                     // toggle data-action
//                     $('a.vote').data('action', previous_action === 'vote' ? 'unvote' : 'vote');
//                     // toggle vote icon
//                     $('i.vote-icon').text(previous_action === 'vote' ? 'thumb_down' : 'thumb_up');
//                     // update total votes
//                     var previous_votes = parseInt($('span.vote-count .total').text());
//                     $('span.vote-count .total').text(previous_action == 'vote' ? previous_votes + 1 : previous_votes - 1);
//                 }
//             });
//     });
// });