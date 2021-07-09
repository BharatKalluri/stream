import { GetServerSidePropsContext } from "next";
import { firebaseAdmin } from "./firebase-admin";
import nookies from "nookies";

export const getUserFromCookie = async (ctx: GetServerSidePropsContext) => {
  const cookies = nookies.get(ctx);
  return await firebaseAdmin.auth().verifyIdToken(cookies.token);
};
