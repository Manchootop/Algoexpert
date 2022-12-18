import { forwardRef, useRef } from "react";

export default function App() {

  return (
    <>
      <MyInput ref={handleRef}/>
      {/* <button onClick={focusInput}>Focus</button> */}
    </>
  );
}

function handleRef(domNode) { 
    console.log(domNode);
}

const MyInput = forwardRef(function (props, ref) {
    return <input ref={ref} {...props} style={{color: 'red'}} />
});

// Mount {initial render} - added for the first time
// updates {re-render}
// Unmount {remove}

// export default function App() {
//   const [isShown, setIsShown] = useState(true);

//   return (
//     <>
//       <button onClick={() => setIsShown(!isShown)}>
//         {isShown ? "Hide Counter" : "Show Counter"}
//       </button>
//       {isShown ? <Counter /> : null}
//     </>
//   );
// }

// function reducer(state, action) {
//     switch (action.type) {
//         case 'increment':
//             return {count: state.count + action.num};
//         case 'decrement':
//             return {count: state.count - action.num}
//         default:
//             throw new Error('Unknown action type')
//     }
// }

// export default function App() {
//   const [state, dispatch] = useReducer(reducer, {
//     count: 0
//   });

//   return (
//     <>
//       <Counter
//       count={state.count}
//       onClick={() => dispatch({
//         type: 'increment',
//         num: 1
//       })}/>

//        <Counter
//       count={state.count}
//       onClick={() => dispatch({
//         type: 'decrement',
//         num: 10
//       })}/>
//     </>
//   );
// }

// function Counter({count, onClick}) {
//   return (
//     <>
//       <button onClick={onClick}>
//         Increment
//         </button>
//       <p>Count: {count}</p>
//     </>
//   );
// }

// export default function App() {
//   return (
//     <>
//     <Comment username="Conner" time={(new Date()).toString()}>
//       <h1>Hello World</h1>
//     </Comment>
//   </>
//   )

// }

// function Comment({username, time, children}) {
//   return (
//     <section>
//       <p>{username} commented at {time}</p>
//       {children}
//     </section>
//   )
// }
