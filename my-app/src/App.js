import React from "react";
import logo from "./logo.svg";
import "./App.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      shoe: [],
    };
  }

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/shoe/")
      .then((res) => res.json())
      .then((data) => this.setState({ shoe: data }));
  }
  render() {
    return (
      <div>
        <ul>
          {this.state.shoe.map((p) => (
            <li>
              <ul>
                <li>size : {p.size}</li>
                <li>Brand Name : {p.brand_name}</li>
                <li>Manufacturer : {p.manufacturer}</li>
                <li>Color : {p.color}</li>
                <li>Material : {p.material}</li>
                <li>Shoe Type : {p.shoe_type}</li>
                <li>Fasten Type : {p.strap}</li>
              </ul>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
