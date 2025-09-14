import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SpamForm from './components/SpamForm';
import SyntheticForm from './components/SyntheticForm';
import ProvenanceForm from './components/ProvenanceForm';
import CategoryForm from './components/CategoryForm';

function App() {
  return (
    <Router>
      <div>
        <h1>JANMARG Content Moderation System</h1>
        <Switch>
          <Route path="/spam" component={SpamForm} />
          <Route path="/synthetic" component={SyntheticForm} />
          <Route path="/provenance" component={ProvenanceForm} />
          <Route path="/category" component={CategoryForm} />
          <Route path="/" exact>
            <h2>Welcome to the JANMARG System</h2>
            <p>Select a service from the menu.</p>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;