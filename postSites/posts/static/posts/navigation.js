$(document).ready(function()
{
	jQuery(".post").append("<hr class='postRule'/>");
	jQuery(".comment").append("<hr class='commentRule'/>");
	addHandlers();
});

function addPost(data){
    // location.reload();
    populatePosts();
     // populateComments();
    $(".message").empty(); 
    $(".message").append('<i class="fa fa-check-circle"></i>'+data.message);
    $(".message").slideToggle();
    $('#text').empty();
	setTimeout(clearMessage,2000)
}

function addComment(data){
    // location.reload();
    populateComments(data.id);
    $(".message").append('<i class="fa fa-check-circle"></i>'+data.message);
    $(".message").slideToggle();
	setTimeout(clearMessage,2000)

}

function clearMessage()
{
	$(".message").slideToggle();
}

function populatePosts()
{
	$.ajax({
	    url: '/posts/viewPosts/',
	    success: function(){
	        $('#wrapper').load('/posts/viewPosts/');
	    },
	});
}

function populateComments(post_id)
{
	$.ajax({
	    url: '/posts/'+post_id+'/viewComments/',
	    success: function()
	    {
	    	id = "#comments_"+post_id;
	        $(id).load('/posts/'+post_id+'/viewComments/');
	        // $(id).css("color":"green");
	    },
	});
}

function addHandlers()
{

	$(".viewComments").click(function()
	{
		$(this).next(".comments").slideToggle();
		$(this).next().next(".addComment").slideToggle();
		$(this).toggleClass("active");
		if($(this).hasClass("active"))
		{
			$(this).text("Hide Comments");
		}
		else
		{
			$(this).text("Show Comments");
		}
	});

	$("#addPostBtn").click(function()
	{
		content = $('#text').val();
		// alert(content); 
		Dajaxice.posts.addPost(addPost,{'text':content});
		$(".message").val(''); 

	});

	$(".addCommentBtn").click(function()
	{
		id = $(this).parent().parent().attr("id").replace("comments_","");
		content = $(this).prev(".addCommentContent").val();
		Dajaxice.posts.addComment(addComment,{'postID':id,'text':content});
		$(this).prev(".addCommentContent").val('');
	});

}