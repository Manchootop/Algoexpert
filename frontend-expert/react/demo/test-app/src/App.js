import { useState } from "react";
import Profile from "./Profiles";
import { UserContext } from "./UserContext";

const Clement = {
  name: "Clement",
  course: "AlgoExpert",
};

const connor = {
  name: "Connor",
  course: "FrontendEpxert",
};

export default function App() {
  const [user, setUser] = useState(conner);

  const toggleUser = () => {
    if (user === conner) {
      setUser(clement);
    } else {
      setUser(conner);
    }
  };
  
  return (
    <main>
        <UserContext.Provider value={user}>
        <Profile />

        </UserContext.Provider>
        <button onClick={toggleUser}>Toggle Users</button>
    </main>
  )
}
