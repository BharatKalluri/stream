import type { NextApiRequest, NextApiResponse } from "next";

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<{ status: boolean }>
) {
  res.status(200).json({ status: true });
}
