// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from "@firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB3hHzO74n2avJWVnfHen6CK0ZJYDxWSV8",
  authDomain: "fir-resumegpt.firebaseapp.com",
  projectId: "fir-resumegpt",
  storageBucket: "fir-resumegpt.appspot.com",
  messagingSenderId: "609779248808",
  appId: "1:609779248808:web:9e2c10f6d940df44701c9d",
  measurementId: "G-W7KXGHZ7JK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const firestore = getFirestore(app)
const analytics = getAnalytics(app);