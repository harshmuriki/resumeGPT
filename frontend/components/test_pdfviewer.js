import React, { useState } from "react";

const Home = () => {
    const [zoomLevel, setZoomLevel] = useState(100); // Initial zoom level

    const handleOpen = () => {
        // Open the PDF or trigger the modal as needed
    };

    const handleZoomIn = () => {
        setZoomLevel(zoomLevel + 10); // Increase the zoom level by 10% (adjust as needed)
    };

    const handleZoomOut = () => {
        setZoomLevel(zoomLevel - 10); // Decrease the zoom level by 10% (adjust as needed)
    };

    return (
        <div>
            <button onClick={handleOpen}>Open PDF</button>
            <div className="relative">
                <button onClick={handleZoomIn}>Zoom In</button>
                <button onClick={handleZoomOut}>Zoom Out</button>
                <div className="overflow-hidden" style={{ width: '100%', height: '600px' }}>
                    <embed
                        className="w-full h-full transform"
                        type='application/pdf'
                        src={"/data.pdf"} // Adjust this path according to your PDF location
                        style={{ transform: `scale(${zoomLevel / 100})` }} // Apply the scale based on zoom level
                    />
                </div>
            </div>
        </div>
    );
};

export default Home;
