import React, { Component } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import "antd/dist/antd.css";
import BaseRouter from "./routes";
// everytime you want to add a new path the baseRouter will do it for you

import CustomLayout from "./containers/Layout";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
    );
  }
}

export default App;
