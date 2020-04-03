import React from "react";
import axios from "axios";

export default function Home() {
  const test_service1 = e => {
    console.log("Testing log one1");

    axios.get("http://localhost:5000/test").then(res => {
      console.log(res.data);
    });
  };

  const test_service2 = e => {
    console.log("Testing log two");

    axios.get("http://localhost:5001/test").then(res => {
      console.log(res.data);
    });
  };

  return (
    <div>
      <h1>Hello</h1>

      <button onClick={test_service1}>Test service 1</button>
      <br />
      <button onClick={test_service2}>Test service 2</button>
    </div>
  );
}
