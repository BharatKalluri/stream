import React from "react";

import { GetServerSidePropsContext } from "next";
import Layout from "../components/layout";
import withPrivateServerSideProps from "../lib/guards/server-side-props-auth.guard";
import { getUserFromCookie } from "../lib/services/auth";

interface IProps {
  message: string;
}

export const getServerSideProps = withPrivateServerSideProps(
  async (ctx: GetServerSidePropsContext): Promise<{ props: IProps }> => {
    const user = await getUserFromCookie(ctx);
    return { props: { message: `User details ${user.email}` } };
  }
);

function AuthenticatedPage(props: IProps) {
  return (
    <Layout title={"Authenticated page"}>
      <p>{props.message}</p>
    </Layout>
  );
}

export default AuthenticatedPage;
