import WelcomeBanner from "./WelcomeBanner";
import Course from "./Course";
import { UserContext } from "./UserContext";
import { useContext } from "react";

export default function Profile() {
  const user = useContext(UserContext)

  return (
    <>
      <WelcomeBanner user={user} />
      <Course user={user} />
    </>
  );
}
