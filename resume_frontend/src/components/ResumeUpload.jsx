import React from 'react';
import { useState } from 'react';

export default function ResumeUpload() {

    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {
      const file = event.target.files[0];
      setSelectedFile(file);
    };

    const handleUpload = () => {
        alert("File uploaded successfully")
    }

  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      if (selectedFile) {
        const formData = new FormData();
        formData.append('file', selectedFile);
  
        // try {
        //   const response = await fetch('/your-upload-endpoint', {
        //     method: 'POST',
        //     body: formData,
        //   });
  
        //   if (response.ok) {
        //     alert('File uploaded successfully!');
        //     setSelectedFile(null);
        //   } else {
        //     alert('File upload failed.');
        //   }
        // } catch (error) {
        //   console.error('Error uploading file:', error);
        //   alert('File upload failed.');
        // }
      }
    };
  
    return (
      <div>
        <h2>File Upload</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="file"
            accept=".csv, .xlsx, .pdf"
            onChange={handleFileChange}
          />
          <button type="submit" disabled={!selectedFile} onClick={handleUpload}>
            Upload File
          </button>
        </form>
      </div>
    );
}

 

  





