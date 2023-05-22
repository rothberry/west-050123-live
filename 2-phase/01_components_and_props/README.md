# Components & Props

### SWBATs:

- [ ] Review the benefits of React over Vanilla JS
- [ ] Review the difference between HTML and JSX
- [ ] Review the importance of Components
- [ ] Review how a component is written
- [ ] Explain what props are and how to create them
- [ ] Recognize destructured props and how to work with them
- [ ] Recognize best practices when writing components and props
- [ ] Observe how to render multiple components from a list

### Creating a React App

`create-react-app` will build a project folder for our application and install all the dependencies we need (via Node Package Manager).

To create a new React application and start it, run:

```
npx create-react-app app-name
cd app-name
npm start
```

In addition to React, it gives us:

- Webpack: a tool for bundling and minifying our code (along with a server for running our code in development)
- Babel: a transpiler that lets us write modern JavaScript and JSX

Other Tools for creating a React App

- [Vite](https://vitejs.dev/guide/)

### Components

Components are the building blocks of React. A component is a function that:

- Takes in some raw data (props)
- Returns user interface (JSX)

There are some things you'll need to keep in mind:

- The name of your component function must be capitalized. This will not work
- A component can only return one element. That element can have children, like this:

```js
function Card() {
  return (
    <div id="card1" className="card">
      <h1>hi</h1>
      <p>wassup?</p>
    </div>
  );
}
```

### Props

When you create components, one way to make them dynamic and reusable is by passing in props. For example, if we wanted to create several cards on our page using a Card component, we could do so like this:

```js
function Card(props) {
  return (
    <div id="card1" className="card">
      <h1>{props.greeting}</h1>
      <p>{props.subGreeting}</p>
    </div>
  );
}

ReactDOM.render(
  <div>
    <Card greeting="hi" subGreeting="hello" />
    <Card greeting="sup" subGreeting="what's up" />
  </div>,
  document.getElementById("root")
);
```

The props argument in our Card component defines an object that React will pass to our function when it is called, and it will use whatever attributes we add to our JSX component as key-value pairs on that props object.

### Resources

- [React](https://reactjs.org/)
- [Babel](https://babeljs.io/)
- [Creating React Apps](https://reactjs.org/docs/create-a-new-react-app.html)
- [create-react-app](https://create-react-app.dev/docs/getting-started)
- [Webpack](https://webpack.js.org/)
- [Quick intro to Webpack](https://medium.com/the-self-taught-programmer/what-is-webpack-and-why-should-i-care-part-1-introduction-ca4da7d0d8dc)

### VSCode extensions

- [draw.io integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Tabnine](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode)
- [ES7+ React/Redux/React-Native/JS snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets)