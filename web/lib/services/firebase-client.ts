import firebaseClient from "firebase/app";
import "firebase/auth";

const GoogleAuthProvider = firebaseClient.auth.GoogleAuthProvider;

const CLIENT_CONFIG = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
};

if (!firebaseClient.apps.length && typeof window !== "undefined") {
  firebaseClient.initializeApp(CLIENT_CONFIG);
  firebaseClient
    .auth()
    .setPersistence(firebaseClient.auth.Auth.Persistence.SESSION)
    .catch((reason) => console.error(reason));
  (window as any).firebase = firebaseClient;
}

export const googleLogin = async () => {
  const provider = new GoogleAuthProvider();
  await firebaseClient.auth().signInWithPopup(provider);
};

export const logout = async () => {
  await firebaseClient.auth().signOut();
};

export { firebaseClient };
