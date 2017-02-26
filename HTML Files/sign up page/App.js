import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
      <link rel="stylesheet" type="text/css"
          href="https://fonts.googleapis.com/css?family=Raleway"/>
        <div className="App-header">
          <h2>Sign Up for Eduya</h2>
        </div>
        <div className="User-Info">
        {/* add action:"server" to form tag */}
        
    <form>
        <br/>
          Name<br/>
          <input type="text" name="nameStr" placeholder="Your name"/><br/><br/>
          Email<br/> 
          <input type="text" name="email" placeholder="Your email"/><br/><br/>
          Username<br/>
          <input type="text" name="username" placeholder="Username"/><br/><br/>
          Password<br/>
          <input type="text" name="password" placeholder="Password"/><br/><br/>
          Do you want to Tutor?: <input type="checkbox" name="email"/><br/><br/>
          <input type="submit" value="Submit" id="submit"/>
        </form>
        </div>
      </div>
    );
  }
}

export default App;
