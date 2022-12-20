import { useState } from "react";
import { Profiles } from './Profiles'
const conner = {
    name: 'Conner',
    course: 'FrontendExpert'
};

const clement = {
    name: 'Clement',
    course: 'AlgoExpert'
};


export default function App(){
    const [user, setUser] = useState(conner);

    const toggleUser = () => {
        if (user === conner) {
            setUser(clement);
        } else {
            setUser(conner);
        }
    }

    return (
        <main>
            <Profiles user={user}/>
            <button onClick={toggleUser}>Toggle User</button>
        </main>
    );
}