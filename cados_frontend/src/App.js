import './App.css';
import HomePage from './pages/HomePage';
import AdvocatePage from './pages/AdvocatePage';
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom' 

function App() {
  return (
    <Router>
      <Routes>
        <Route element={<HomePage/>} path=""></Route>
        <Route element={<AdvocatePage/>} path="/advocate/:username"></Route>
      </Routes>
    </Router>
  );
}

export default App;
