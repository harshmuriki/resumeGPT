import React from 'react';
import { useState, useEffect } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

export default function JobDescription() {
    return (
    <div>
        <TextField
            label="Enter link to job description"
            color="secondary"
            variant="outlined"
            fullWidth
            style={{marginBottom: '1vw'}}
        />
        <Button variant="contained" color="primary">
            Submit
        </Button>
    </div>
    )
}