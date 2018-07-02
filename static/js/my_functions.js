	function update_document(json_response){
		// Taking the new values to update the page
		var new_id = json_response["id"];
	    var new_title = json_response["title"];
	    var new_image_link = json_response["image_link"];
	    var new_image_alt = json_response["image_alt"];
	    var new_original_url = json_response["original_url"];

	    // Chaning correspondent elements
	    $("#comic").parent().prop('id', new_id);
	    document.getElementById("comic").textContent=new_title;
	    $("#image").prop("src",new_image_link);
	    $("#image").prop("alt",new_image_alt);
	    $("#original_url").prop("href",new_original_url);
	    document.getElementById("original_url").textContent= original_url;
	}

	function retrieveComic(action_taken, current_comic_id){
			var parameters = {
				mode: action_taken,
				id: current_comic_id
			};
	    	$.ajax({
	            url: '/retrieve_comic/',
	            data: JSON.stringify(parameters),
	            type: "POST",
	            success: function(response) {
	            	json_response =JSON.parse(response);
	            	update_document(json_response);
	            },
	            error: function(error) {
	                alert("The comic you want to retrieve doesn't exist")
	            }
        	});
	}
