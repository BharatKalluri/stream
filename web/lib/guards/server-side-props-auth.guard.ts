import { GetServerSideProps, GetServerSidePropsContext } from "next";
import { firebaseAdmin } from "../services/firebase-admin";
import nookies from "nookies";

const FALLBACK_IF_NO_AUTH_ROUTE = "/";

const isAuthenticated = async (ctx: GetServerSidePropsContext) => {
  try {
    const cookies = nookies.get(ctx);
    await firebaseAdmin.auth().verifyIdToken(cookies.token);
    return true;
  } catch (e) {
    return false;
  }
};

export default function withPrivateServerSideProps<P>(
  getServerSidePropsFunc?: GetServerSideProps
): GetServerSideProps {
  return async (ctx: GetServerSidePropsContext) => {
    const _isAuthenticated = await isAuthenticated(ctx);

    if (!_isAuthenticated) {
      return {
        redirect: {
          destination: `${FALLBACK_IF_NO_AUTH_ROUTE}?redirectTo=${ctx.resolvedUrl}`,
          permanent: false,
        },
      };
    }

    if (getServerSidePropsFunc) {
      return await getServerSidePropsFunc(ctx);
    }
    return { props: {} };
  };
}
