import React, { lazy, Suspense } from "react";
import "./App.css";

import { Provider } from "react-redux";

import store from "./store";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

const AddUser = lazy(() => import("./components/AddUser"));
const Home = lazy(() => import("./components/Home"));
function App() {
  return (
    <Provider store={store}>
      <Router>
        <Suspense
          fallback={
            <div>
              <h2>Loading.....ss </h2>
            </div>
          }
        >
          <Switch>
            <Route exact path="/" component={Home}></Route>
            <Route exact path="/home" component={Home}></Route>
            <Route exact path="/add" component={AddUser}></Route>
          </Switch>
        </Suspense>
      </Router>
    </Provider>
  );
}

export default App;
