		$("#seeAnotherField").change(function() {
		  if ($(this).val() == "c") {
		    $('#institudeFieldDiv').show();
		    $('#otherField').attr('required', '');
		    $('#otherField').attr('data-error', 'This field is required.');
		  }

		  if ($(this).val() == "t") {
		  	alert("Ok i am");
		    $('#teacherFieldDiv').show();
		    $('#otherField').attr('required', '');
		    $('#otherField').attr('data-error', 'This field is required.');
		  }
		  if ($(this).val() == "s") {
		    $('#studentFieldDiv').show();
		    $('#otherField').attr('required', '');
		    $('#otherField').attr('data-error', 'This field is required.');
		  }

		  else {
		    $('#institudeFieldDiv').hide();
		    $('#teacherFieldDiv').hide();
		    $('#studentFieldDiv').hide();
		    $('#otherField').removeAttr('required');
		    $('#otherField').removeAttr('data-error');
		  }
		});
		$("#seeAnotherField").trigger("change");
