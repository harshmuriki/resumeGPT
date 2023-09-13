import React, { useRef } from 'react';
import { useState } from 'react';
import {firestore} from "../firebase"
import { addDoc, collection } from "@firebase/firestore"
export default function ResumeUpload() {

    const [selectedFile, setSelectedFile] = useState(null);
    const fileRef = useRef()
    const ref = collection(firestore, "resume_file")

    const handleFileChange = (event) => {
      const file = event.target.files[0];
      setSelectedFile(file);
    };

    const handleUpload = async (e) => {
      e.preventDefault();
      alert("File uploaded successfully")

      let data = {
        file: fileRef.current.value,
      }

      try {
        addDoc(ref, data)
      } catch (e) {
          console.log(e);
      }
    }

  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      if (selectedFile) {
        const formData = new FormData();
        formData.append('file', selectedFile);
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
          <button type="submit" ref={fileRef} disabled={!selectedFile} onClick={handleUpload}>
            Upload File
          </button>
        </form>
      </div>
    );
}

 

  





