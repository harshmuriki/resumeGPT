import React from 'react';
import { useState, useEffect } from 'react';
import { ref, uploadBytes, getDownloadURL, listAll, list } from "firebase/storage";
import { storage } from "../firebase";
import { v4 } from 'uuid';

export default function ResumeUpload() {

    const [fileUpload, setFileUpload] = useState(null);
    const [fileUrls, setFileUrls] = useState([])

    const filesListRef = ref(storage, "files/")
    const handleUpload = () => {
      console.log(fileUpload)
      if (fileUpload == null) 
        return;
      const fileRef = ref(storage, `files/${fileUpload.name + v4()}`)

      uploadBytes(fileRef, fileUpload).then((snapshot) => {
        getDownloadURL(snapshot.ref).then((url) =>{
          setFileUrls((prev) => [...prev, url])
        })
      })
    }

    useEffect(() => {
      listAll(filesListRef).then((response) => {
        response.items.forEach((item) => {
          getDownloadURL(item).then((url) => {
            setFileUrls((prev) => [...prev, url]);
          });
        });
      });
    }, []);
  
    return (
      <div>
          <input
            type="file"
            accept=".csv, .xlsx, .pdf"
            onChange={(event) => {
              setFileUpload(event.target.files[0])
            }}
          />
          <button type="submit" onClick={handleUpload}>
            Upload
          </button>
          {fileUrls.map((url) => {
            return <img src={url} />
          })}
      </div>
    );
}

 

  





