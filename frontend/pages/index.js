import React, {} from "react";
import { pdfjs } from 'react-pdf'
import Pdfcomp from "@/components/pdfcomp";

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
    'pdfjs-dist/build/pdf.worker.min.js',
    import.meta.url,
).toString();

const Index = () => {
    return (
        <div>
            {/* <Document file="somefile.pdf" /> */}
            <h1>PDF Viewer</h1>
            <Pdfcomp />
        </div>
    );
}

export default Index;