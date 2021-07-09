import { useAuth } from "./auth-context";
import { googleLogin, logout } from "../lib/services/firebase-client";
import { Button } from "@chakra-ui/react";

const UserAuthButton = () => {
  const { user } = useAuth();
  if (user) {
    return <Button onClick={logout}>Log out {user.displayName}?</Button>;
  }
  return <Button onClick={googleLogin}>Log in with google</Button>;
};

export default UserAuthButton;
