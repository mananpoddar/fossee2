
        var inputDocument = document.getElementById('inputDocument');
        var fileList = [];
        
        inputDocument.addEventListener('change',function(e){
            for(var i =0;i<inputDocument.files.length;i++){
                console.log(inputDocument.files[i].name);

                //check if the extension of file is valid
                name = String(inputDocument.files[i].name);
                var l = name.split(".",2);
                var extn = String(l[1]);
                //if valid sendFile otherwise not
                if(extn.localeCompare('doc')==0||extn.localeCompare('docx')==0||extn.localeCompare('pdf')==0){
            
                    var node = document.createElement("LI");                 // Create a <li> node
                    var textnode = document.createTextNode(name);         // Create a text node
                    node.appendChild(textnode);                              // Append the text to <li>
                    document.getElementById("displayFile").appendChild(node);
                    fileList.push(inputDocument.files[i]);
                    console.log('sending Document');
                }
                else{
                    console.log("it's not a valid extension");
                    var node = document.createElement("LI");                 // Create a <li> node
                    var textnode = document.createTextNode("only doc,docx and pdf's are allowed, please enter valid file extensions");         // Create a text node
                    node.appendChild(textnode);                              // Append the text to <li>
                    document.getElementById("displayFile").appendChild(node);
                }


               
            }
        })
      
        var fileCatcher = document.getElementById('file-catcher')
        fileCatcher.addEventListener('submit',function(e){
            e.preventDefault();
            console.log(fileList.length)
            fileList.forEach(function(file){
                sendFile(file); 
                
            });
           //after sending all the files making a get request to viewDocument 
          window.location.href="/fossee2/successfullyUploaded";

        });
        
        sendFile = function(file){
           
            var title       =   document.getElementById('title').value
            var description =   document.getElementById('description').value
        
            var formData = new FormData();
            formData.append("Document",file)
            formData.append("title",title)
            formData.append("description",description)


          
            jQuery.ajax({
                url: "",
                type: "POST",
                data:formData,
                processData: false,
                contentType: false,
                success:function(){
                    console.log("done successfully");
                }
            });
        };