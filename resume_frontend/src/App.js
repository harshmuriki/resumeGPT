import logo from './logo.svg';
import './App.css';
import ResumeUpload from './components/ResumeUpload';
import JobDescription from './components/JobDescription';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div>
          <div style={{marginBottom: '5vw'}}>
            <ResumeUpload/>
          </div>
          <JobDescription/>
          </div>
      </header>
    </div>
  );
}

export default App;
