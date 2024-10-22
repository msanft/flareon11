using System;
using Org.BouncyCastle.Math;
using Org.BouncyCastle.Security;
using Org.BouncyCastle.Math.EC;

class Program
{
    static void Main(string[] args)
    {
        Init();
    }

    static void Init()
    {
        BigInteger p = new BigInteger("c90102faa48f18b5eac1f76bb40a1b9fb0d841712bbe3e5576a7a56976c2baeca47809765283aa078583e1e65172a3fd", 16);
        Console.WriteLine($"P: {p}");

        BigInteger a = new BigInteger("a079db08ea2470350c182487b50f7707dd46a58a1d160ff79297dcc9bfad6cfc96a81c4a97564118a40331fe0fc1327f", 16);
        Console.WriteLine($"A: {a}");

        BigInteger b = new BigInteger("9f939c02a7bd7fc263a4cce416f4c575f28d0c1315c4f0c282fca6709a5f9f7f9c251c9eede9eb1baa31602167fa5380", 16);
        Console.WriteLine($"B: {b}");

        FpCurve curve = new FpCurve(p, a, b, null, null);

        BigInteger serverX = new BigInteger("b3e5f89f04d49834de312110ae05f0649b3f0bbe2987304fc4ec2f46d6f036f1a897807c4e693e0bb5cd9ac8a8005f06", 16);
        BigInteger serverY = new BigInteger("85944d98396918741316cd0109929cb706af0cca1eaf378219c5286bdc21e979210390573e3047645e1969bdbcb667eb", 16);

        ECPoint serverP = curve.CreatePoint(serverX, serverY);
        Console.WriteLine($"Server P: {serverP}");

        BigInteger secret = new BigInteger("7ed85751e7131b5eaf5592718bef79a9", 16);

        ECPoint sharedP = serverP.Multiply(secret).Normalize();

        BigInteger sharedX = sharedP.AffineXCoord.ToBigInteger();

        Byte[] sharedXBytes = sharedX.ToByteArray();

        String sharedXHex = Convert.ToHexString(sharedXBytes);
        Console.WriteLine($"Shared X: {sharedXHex}");

        return;
    }
}
