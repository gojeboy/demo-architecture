import { applyMiddleware, compose, createStore } from "redux";
import rootReducer from "./reducers";
import thunk from "redux-thunk";

const initialState = {};
const middleware = [thunk];

const env = process.env.ENV;

const compose_store = () => {
  if (env.lowercase() == "dev") {
    compose(
      applyMiddleware(...middleware),
      window.__REDUX_DEVTOOLS_EXTENSION__ &&
        window.__REDUX_DEVTOOLS_EXTENSION__()
    );
  } else {
    compose(applyMiddleware(...middleware));
  }
};

export default createStore(rootReducer, initialState, compose_store());
